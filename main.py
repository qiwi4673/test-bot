import discord
from discord.ext import commands

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# ボットがオンラインになったときのイベント
@client.event
async def on_ready():
    print(f'{client.user}としてログインしました。')
    print('------')

# メッセージが送られたときのイベント
@client.event
async def on_message(message):
    # ボット自身のメッセージを無視
    if message.author == client.user:
        return

    # メッセージが "ping" で始まっていたら
    if message.content.startswith('ping'):
        await message.channel.send('pong!')

# トークンを設定してボットを実行
# client.run('YOUR_BOT_TOKEN_HERE')
