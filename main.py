import discord
import os
import random
import json
from keep_alive import keep_alive

# 1. ユーザーデータの読み込みと保存
def load_currency():
    try:
        with open('currency.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_currency(currency_data):
    with open('currency.json', 'w') as f:
        json.dump(currency_data, f, indent=4)

currency = load_currency()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="お料理"))

    @client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.bot:
        return
    
    user_id = str(message.author.id)

    # ユーザーが辞書に存在しない場合は初期化
    if user_id not in currency:
        currency[user_id] = 0
        save_currency(currency)

    # '!balance' コマンドで残高を表示
    if message.content.startswith('!balance'):
        await message.channel.send(f'{message.author.mention}の現在の残高は {currency[user_id]} コインです。')

    # '!earn' コマンドで通貨を増やす
    elif message.content.startswith('!earn'):
        earned = random.randint(1, 10)
        currency[user_id] += earned
        save_currency(currency)
        await message.channel.send(f'{message.author.mention}は {earned} コインを獲得しました！')

    # '!spend' コマンドで通貨を消費
    elif message.content.startswith('!spend'):
        try:
            # コマンドから消費する金額を取得
            amount_to_spend = int(message.content.split()[1])

            if amount_to_spend <= 0:
                await message.channel.send('消費する金額は1以上で指定してください。')
                return

            # 残高が十分かチェック
            if currency[user_id] >= amount_to_spend:
                currency[user_id] -= amount_to_spend
                save_currency(currency)
                await message.channel.send(f'{message.author.mention}は {amount_to_spend} コインを消費しました。')
            else:
                await message.channel.send(f'{message.author.mention}、残高が足りません。')
        except (IndexError, ValueError):
            # 金額が指定されていないか、数字でない場合のエラー処理
            await message.channel.send('使い方が間違っています。`!spend <金額>` のように入力してください。')


    

    
    # 特定のメッセージへの応答
    if message.content.startswith('ぼれろ、ごはん'):
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
            'ン浪の奢りで焼肉'
        ]
        await message.channel.send(random.choice(responses))
    
    elif message.content == 'たけ':
        dice_result = random.randint(1, 100)
        
        result_text = ''
        if dice_result <= 5:
            result_text = '🟨クリティカル！'
        elif dice_result >= 96:
            result_text = '🟪ファンブル...'
        await message.reply(f'rolled: **{dice_result}** \n{result_text}')

    if 'たの' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)
    
    if 'タノ' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

    if '頼ん' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

    if '田野' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)
    
    if '頼もしい' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

    if '頼み' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

    if 'TANO' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

    
    if '楽しい' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

    if '楽しみ' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)
    
    if message.content.startswith('ぼれろ、こんだて'):
        subject = ['そば', 'フカヒレスープ', 'パフェ', '小籠包', 'レモン', 'アイスクリーム', 'シュウマイ', 'スープ', '寿司', '春巻き', 'ワッフル', 'ローストチキン', 'シリアル', 'パスタ', 'カツ丼', 'カヌレ', 'フレンチトースト', 'オレンジジュース', '酢豚', '餃子', 'プリン', 'もつ鍋', 'クリームチーズ', 'パンケーキ', 'ナッツ', 'カレーライス', 'ホットドッグ', 'ショートケーキ', 'フォンダンショコラ', 'スパゲッティ', 'クロワッサン', 'サンドイッチ', 'ミルク', '親子丼', '紅茶', 'しゃぶしゃぶ', 'エビフライ', 'トマト鍋', 'ハンバーガー', 'ドーナツ', 'ピザ', '麻婆豆腐', '北京ダック', '牛丼', 'たこ焼き', 'うどん', 'マカロン', 'パンナコッタ', 'フライドポテト', '天ぷら', '味噌汁', '回鍋肉', 'キムチ鍋', 'クッキー', 'ラーメン', 'クレープ', '焼き肉', 'エビチリ', 'コーヒー', 'マフィン', 'チーズケーキ']
        action = [
            "を焼いたもの", "を煮たもの", "を炒めたもの", "を揚げたもの", "を蒸したもの",
            "茹でたもの", "を炙ったもの", "を和えたやつ", "を漬けたもの", "を燻したもの",
            "を蒸し焼きにしたもの", "の炒め煮", "を炊いたもの", "の網焼き", "の串焼き",
            "のソテー", "のグリル", "をローストしたもの", "のポシェ", "をフランベしたもの"
        ]
        random_subject = random.choice(subject)
        random_action = random.choice(action)
        await message.channel.send(f'{random_subject}{random_action}はどうかな？')

    # メッセージの長さによって返信を変える新しいロジック
    if message.content.startswith('ぼれろ〜'):
        # メッセージが「ぼれろ〜」のみの場合
        if len(message.content.strip()) == 4:
            commonreply = ['どうしました〜？','なぁに〜？','ん〜？','とってもすごいBoleroです！']
            random_commonreply = random.choice(commonreply)
            await message.channel.send(f'{random_commonreply}')
        # 5文字以上の場合
        elif len(message.content) > 4:
            agreement =['うんうん','たしかに','そっか','知らなかった','すごく','はい','えっとね','えっ','へぇ〜','なんと','でも','まじか','わっ']
            letter = ['おなかすいたね','のどかわいたね','ねむいね','おはようの時間だね','いいね','おやすみの時間だね','ナントの勅令だよ','土砂降りだ','おばけかも','かっこいい','とても晴れてるよ']
            random_agreement = random.choice(agreement)
            random_letter = random.choice(letter)
            await message.channel.send(f'{random_agreement}、{random_letter}〜。')

    if message.content.startswith('ぼれろ、えもじ'):
        animal_emojis = [
    '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯',
    '🦁', '🐮', '🐷', '🐸', '🐵', '🐒', '🐔', '🐧', '🦅', '🦉',
    '🐴', '🦄', '🐺', '🐗', '🐘', '🦏', '🦌', '🐊', '🐉', '🦖',
    '🦕', '🐢', '🐍', '🐙', '🐠', '🐳', '🐝', '🐞', '🐦‍🔥', '🐌'
]
        random_emoji = random.choice(animal_emojis)
        await message.add_reaction(random_emoji)

    # メッセージの末尾が「かな？」で終わるかチェック
    if message.content.strip().endswith('かな？'):
        questionagree = ['うん、','えっ','う〜ん','ん〜']
        questionletter = ['違うかも〜','そうかも〜','違うよ〜','そうだよ〜']
        random_questionagree = random.choice(questionagree)
        random_questionletter = random.choice(questionletter)
        await message.channel.send(f'{random_questionagree}{random_questionletter}。')


TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
client.run(TOKEN)
