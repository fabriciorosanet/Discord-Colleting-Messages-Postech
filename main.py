import discord
from discord.ext import commands
import pandas as pandas
from pytz import timezone
from dotenv import load_dotenv
import os
from pymongo import MongoClient  

load_dotenv()  

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')  
MONGODB_URI = os.getenv('MONGODB_URI')  
DATABASE_NAME = 'discord_canal_duvidas'  
COLLECTION_NAME = '6/7SOAT'  

CHANNEL_ID = int(os.getenv('CHANNEL_ID'))  
GUILD_ID = int(os.getenv('GUILD_ID'))      

client = MongoClient(MONGODB_URI)
try:
    client.admin.command('ping')
    print("Conectado ao MongoDB com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    exit()

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

        guild = bot.get_guild(GUILD_ID)
        if guild is None:
            print(f'Servidor com ID {GUILD_ID} não encontrado.')
            return

        channel = guild.get_channel(CHANNEL_ID)
        if channel is None or channel.type != discord.ChannelType.forum:
            print(f'Canal com ID {CHANNEL_ID} não encontrado ou não é um canal de fórum no servidor {guild.name}.')
            return

        print(f'Extraindo mensagens do canal: {channel.name} no servidor: {guild.name}')

        for thread in channel.threads:
            print(f'Extraindo mensagens do tópico: {thread.name}')
            async for message in thread.history(limit=None):
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

        if messages_data:
            result = collection.insert_many(messages_data)
            print(f'{len(result.inserted_ids)} mensagens foram inseridas no MongoDB.')
        else:
            print("Nenhuma mensagem foi coletada para inserir no MongoDB.")

        await bot.close()

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        await bot.close()

bot.run(DISCORD_TOKEN)