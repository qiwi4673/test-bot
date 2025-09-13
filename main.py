import discord
import os
from keep_alive import keep_alive

# メッセージ内容を読み取るためのインテントを有効化
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    # ボット自身のメッセージには反応しないようにする
    if message.author == client.user:
        return

    # メッセージに 🐌 の絵文字を追加
    emoji = "🐌"
    await message.add_reaction(emoji)

    # メッセージの内容が 'hello' で始まる場合、'Hello!' と返信する
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバーの立ち上げ
keep_alive()
client.run(TOKEN)
