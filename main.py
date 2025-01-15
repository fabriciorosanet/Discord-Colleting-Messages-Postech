import discord
from discord.ext import commands
import pandas as pd
from pytz import timezone
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient
import sys

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
MONGODB_URI = os.getenv('MONGODB_URI')

# Leitura das datas de início e fim
START_DATE_STR = os.getenv('START_DATE', '2024-01-01')
END_DATE_STR = os.getenv('END_DATE', '2024-12-31')

# Converte as strings de data no formato YYYY-MM-DD para objetos datetime
start_date = datetime.strptime(START_DATE_STR, '%Y-%m-%d')
end_date = datetime.strptime(END_DATE_STR, '%Y-%m-%d')

DATABASE_NAME = 'discord_bot-2024'
COLLECTION_NAME = '2024-01-01 a 2024-12-31'

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

messages_data = []
saopaulo_tz = timezone('America/Sao_Paulo')

@bot.event
async def on_ready():
    try:
        print(f'Logged in as {bot.user.name}')
        print(f'Coletando mensagens entre {start_date} e {end_date}')

        for guild in bot.guilds:
            print(f"Coletando mensagens do servidor: {guild.name}")

            for channel in guild.text_channels:
                # Histórico do canal no intervalo de datas
                async for message in channel.history(after=start_date, before=end_date):
                    if isinstance(message.author, discord.Member):
                        role_name = message.author.top_role.name if message.author.top_role else "None"
                    else:
                        role_name = "None"

                    messages_data.append({
                        "Message": message.content,
                        "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                        "User": message.author.name,
                        "Role": role_name,
                        "Channel": channel.name,
                        "Thread": "None",
                        "Server Name": guild.name,
                        "Category": channel.category.name if channel.category is not None else "None"
                    })

                # Histórico das threads do canal no intervalo de datas
                for thread in channel.threads:
                    async for message in thread.history(after=start_date, before=end_date):
                        if isinstance(message.author, discord.Member):
                            role_name = message.author.top_role.name if message.author.top_role else "None"
                        else:
                            role_name = "None"

                        messages_data.append({
                            "Message": message.content,
                            "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                            "User": message.author.name,
                            "Role": role_name,
                            "Channel": channel.name,
                            "Thread": thread.name,
                            "Server Name": guild.name,
                            "Category": channel.category.name if channel.category is not None else "None"
                        })

            # Histórico de fóruns (nem todo servidor possui)
            if hasattr(guild, 'forums') and guild.forums:
                for forum in guild.forums:
                    for thread in forum.threads:
                        async for message in thread.history(after=start_date, before=end_date):
                            if isinstance(message.author, discord.Member):
                                role_name = message.author.top_role.name if message.author.top_role else "None"
                            else:
                                role_name = "None"

                            messages_data.append({
                                "Message": message.content,
                                "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                                "User": message.author.name,
                                "Role": role_name,
                                "Channel": forum.name,
                                "Thread": thread.name,
                                "Server Name": guild.name,
                                "Category": forum.category.name if forum.category is not None else "None"
                            })

        if messages_data:
            collection.insert_many(messages_data)
            print(f'{len(messages_data)} mensagens foram inseridas no MongoDB.')

        await bot.close()
        sys.exit(0)

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        await bot.close()
        sys.exit(1)

bot.run(DISCORD_TOKEN)
