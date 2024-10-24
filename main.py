import discord
from discord.ext import commands
import pandas as pd
from pytz import timezone
from datetime import datetime
from dotenv import load_dotenv
import os
from pymongo import MongoClient  

load_dotenv()  

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  
MONGODB_URI = os.getenv('MONGODB_URI')  
DATABASE_NAME = 'discord_bot'  
COLLECTION_NAME = 'mensagem-dos-servidores-01.10-a-24.10'  

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

        for guild in bot.guilds:
            print(guild.name)

            for channel in guild.text_channels:
                async for message in channel.history(after=datetime.fromisoformat('2024-10-01')):

                    messages_data.append({
                        "Message": message.content,
                        "Message Datetime": message.created_at.astimezone(saopaulo_tz),  
                        "User": message.author.name,
                        "Role": message.author.top_role.name if hasattr(message.author, 'top_role') else "None",
                        "Channel": channel.name,
                        "Thread": "None",
                        "Server Name": guild.name,
                        "Category": channel.category.name if channel.category is not None else "None"
                    })

                for thread in channel.threads:
                    async for message in thread.history(after=datetime.fromisoformat('2024-10-01')):

                        messages_data.append({
                            "Message": message.content,
                            "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                            "User": message.author.name,
                            "Role": message.author.top_role.name if hasattr(message.author, 'top_role') else "None",
                            "Channel": channel.name,
                            "Thread": thread.name,
                            "Server Name": guild.name,
                            "Category": channel.category.name if channel.category is not None else "None"
                        })

            for forum in guild.forums:
                for thread in forum.threads:
                    async for message in thread.history(after=datetime.fromisoformat('2024-10-01')):

                        messages_data.append({
                            "Message": message.content,
                            "Message Datetime": message.created_at.astimezone(saopaulo_tz),
                            "User": message.author.name,
                            "Role": message.author.top_role.name if hasattr(message.author, 'top_role') else "None",
                            "Channel": forum.name,
                            "Thread": thread.name,
                            "Server Name": guild.name,
                            "Category": forum.category.name if forum.category is not None else "None"
                        })

        
        if messages_data:
            collection.insert_many(messages_data)
            print(f'{len(messages_data)} mensagens foram inseridas no MongoDB.')

        exit()

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        exit()

bot.run(DISCORD_TOKEN)
