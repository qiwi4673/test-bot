import os
from os.path import dirname, join

import discord
from dotenv import load_dotenv

from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())

load_dotenv(verbose=True)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

@bot.event
async def on_message(message: discord.Message):
    """メッセージをおうむ返しにする処理"""

    if message.author.bot: # ボットのメッセージは無視
        return

    await message.reply(message.content)



TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
