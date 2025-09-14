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

    # 特定のメッセージへの応答
    if message.content.startswith('んろう、ごはん'):  # <-- プレフィックスを追加してコマンドとして扱う
        # ランダムに選ぶ返信のリスト
        responses = [
            'きゅうりの浅漬け',
            'きゅうりの深漬け',
            'きゅうりの漬け物',
            'きゅうりの糠漬け',
            '味噌漬けきゅうり'
        ]
        # リストからランダムに1つ選んで送信
        await message.channel.send(random.choice(responses))
        
    elif message.content == 'たけ':
        # 1から6までの整数をランダムに生成
        dice_result = random.randint(1, 100)
        
        # 結果の判定
        result_text = '' # 結果のテキストを初期化
        if dice_result <= 5:
            result_text = '🟨クリティカル！'
        elif dice_result >= 96:
            result_text = '🟪ファンブル...'
        # 結果を一つのメッセージにまとめてリプライとして送信
        await message.reply(f'rolled: **{dice_result}** \n{result_text}')
    if 'たの' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)
TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
