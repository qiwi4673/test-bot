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
            '味噌漬けきゅうり',
            '一本漬けきゅうり',
            '漬物石',
            'きゅうりの浅漬け',
            'きゅうりの深漬け',
            'きゅうりの漬け物',
            'きゅうりの糠漬け',
            '味噌漬けきゅうり',
            '一本漬けきゅうり',
            '漬物石',
            'きゅうりの浅漬け',
            'きゅうりの深漬け',
            'きゅうりの漬け物',
            'きゅうりの糠漬け',
            '味噌漬けきゅうり',
            '一本漬けきゅうり',
            '漬物石',
            'ン浪の奢りで焼肉'
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
 if message.content.startswith('んろう、こんだて'):
        # 1つ目のランダムな要素のリスト
        subject = ['そば', 'フカヒレスープ', 'パフェ', '小籠包', 'レモン', 'アイスクリーム', 'シュウマイ', 'スープ', '寿司', '春巻き', 'ワッフル', 'ローストチキン', 'シリアル', 'パスタ', 'カツ丼', 'カヌレ', 'フレンチトースト', 'オレンジジュース', '酢豚', '餃子', 'プリン', 'もつ鍋', 'クリームチーズ', 'パンケーキ', 'ナッツ', 'カレーライス', 'ホットドッグ', 'ショートケーキ', 'フォンダンショコラ', 'スパゲッティ', 'クロワッサン', 'サンドイッチ', 'ミルク', '親子丼', '紅茶', 'しゃぶしゃぶ', 'エビフライ', 'トマト鍋', 'ハンバーガー', 'ドーナツ', 'ピザ', '麻婆豆腐', '北京ダック', '牛丼', 'たこ焼き', 'うどん', 'マカロン', 'パンナコッタ', 'フライドポテト', '天ぷら', '味噌汁', '回鍋肉', 'キムチ鍋', 'クッキー', 'ラーメン', 'クレープ', '焼き肉', 'エビチリ', 'コーヒー', 'マフィン']
        # 2つ目のランダムな要素のリスト
        action = [
    "を焼いたもの", "を煮たもの", "を炒めたもの", "を揚げたもの", "を蒸したもの",
    "茹でたもの", "を炙ったもの", "を和えたやつ", "を漬けたもの", "を燻したもの",
    "を蒸し焼きにしたもの", "の炒め煮", "を炊いたもの", "の網焼き", "の串焼き",
    "のソテー", "のグリル", "をローストしたもの", "のポシェ", "をフランベしたもの"
]
        random_subject = random.choice(subject)
        random_action = random.choice(action)
        await message.channel.send(f'{random_subject}{random_action}。')
TOKEN = os.getenv("DISCORD_TOKEN")
# Web サーバの立ち上げ
keep_alive()
client.run(TOKEN)
