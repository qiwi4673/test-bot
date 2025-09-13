import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents))

@client.event
async def on_ready():
    print('ログインしました')

@client.event
if message.author == client.user:
    return

async def on_message(message):
    emoji ="🐌"
    await message.add_reaction(emoji)

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
