import discord
import os
from keep_alive import keep_alive

client = discord.Client(intents=discord.Intents.default())
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')

@client.event
async def on_message(message):
    emoji ="👍"
    await message.add_reaction(emoji)

@client.event
async def on_message(message):
    # Bot自身のメッセージには応答しないようにします
    if message.author == client.user:
        return

    # メッセージの内容が 'hello' だった場合
    if message.content.startswith('hello'):
        # メッセージが送られたチャンネルに 'Hello!' と返信します
        await message.channel.send('Hello!')

keep_alive()

TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    client.run(TOKEN)
else:
    print("Tokenが見つかりませんでした")
