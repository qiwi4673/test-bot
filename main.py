import os
from os.path import dirname, join

import discord
from dotenv import load_dotenv

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


load_dotenv(verbose=True)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="🐌"
    await message.add_reaction(emoji)

@client.event
async def on_message(message):
    # Bot自身のメッセージには応答しないようにします
    if message.author == client.user:
        return

    # メッセージの内容が 'hello' だった場合
    if message.content.startswith('やあ'):
        # メッセージが送られたチャンネルに 'Hello!' と返信します
        await message.channel.send('やあ')

# 開発者ポータルで取得したボットトークンを設定
# client.run('YOUR_BOT_TOKEN_HERE')



TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
