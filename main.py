import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
bomb = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

