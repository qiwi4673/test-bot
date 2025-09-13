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
    if message.content.startswith('んろう、ごはん'):  # <-- プレフィックスを追加してコマンドとして扱う
        # ランダムに選ぶ返信のリスト
        responses = [
            'イチジク',
            'スープ',
            '味噌汁',
            '御御御付'
        ]
        # リストからランダムに1つ選んで送信
        await message.channel.send(random.choice(responses))
    elif message.content.startswith('!roll'):
        # 1から6までの整数をランダムに生成
        dice_result = random.randint(1, 100)
        
        # 結果をメッセージとして送信
        await message.channel.send(f'🎲 サイコロを振りました... 出た目は **{dice_result}** です！')

        # 成功・失敗の判定
        if dice_result <= 5:
            await message.channel.send('✅ 成功です！')
        elif dice_result >= 96:
            await message.channel.send('❌ 失敗です...')
TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
