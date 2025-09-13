import discord
import os
import random
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # 絵文字の追加
    emoji = "🐌"
    await message.add_reaction(emoji)

    # 特定のメッセージへの応答
    if message.content.startswith('hello'):  # <-- プレフィックスを追加してコマンドとして扱う
        # ランダムに選ぶ返信のリスト
        responses = [
            'Hello!',
            'こんにちは！',
            'やあ！',
            'どうも！'
        ]
        # リストからランダムに1つ選んで送信
        await message.channel.send(random.choice(responses))

TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
