import discord
import os
import random
import json
import time  # <-- timeモジュールを追加
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

# 最後に通貨を獲得した時間を記録する辞書
last_earn_times = {}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('ログインしました')
    await client.change_presence(activity=discord.Game(name="おままごと"))

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return

    user_id = str(message.author.id)

    if user_id not in currency:
        currency[user_id] = 0
        save_currency(currency)

    # 全てのコマンドを一つのif/elifチェーンにまとめる
    if message.content.startswith('ぼれろ、しょうかい'):
        await message.channel.send(f'{message.author.display_name}さんの現在の残高は {currency[user_id]} コインです。')

    elif message.content.startswith('ぼれろ、おこづかい'):
        # クールダウンの設定 (秒)
        cooldown_time = 86400
        
        # 最後に獲得した時間をチェック
        if user_id in last_earn_times and (time.time() - last_earn_times[user_id] < cooldown_time):
            remaining_time = int(cooldown_time - (time.time() - last_earn_times[user_id]))
            await message.channel.send(f'{message.author.display_name}さん、もうもらったでしょ〜')
        else:
            # 新しい通貨を獲得
            earned = random.randint(20, 50)
            currency[user_id] += earned
            last_earn_times[user_id] = time.time()  # タイムスタンプを更新
            save_currency(currency)
            await message.channel.send(f'{message.author.display_name}さんに {earned} ターノあげる〜！')

    elif message.content.startswith('!spend'):
        try:
            amount_to_spend = int(message.content.split()[1])
            if amount_to_spend <= 0:
                await message.channel.send('消費する金額は1以上で指定してください。')
                return
            if currency[user_id] >= amount_to_spend:
                currency[user_id] -= amount_to_spend
                save_currency(currency)
                await message.channel.send(f'{message.author.display_name}さんは {amount_to_spend} コインを消費しました。')
            else:
                await message.channel.send(f'{message.author.display_name}さん、残高が足りません。')
        except (IndexError, ValueError):
            await message.channel.send('使い方が間違っています。`!spend <金額>` のように入力してください。')

    elif message.content.startswith('ぼれろ、ごはん'):
        responses = [
            'きゅうりの浅漬け', 'きゅうりの深漬け', 'きゅうりの漬け物', 'きゅうりの糠漬け',
            '味噌漬けきゅうり', '一本漬けきゅうり', '漬物石', 'ン浪の奢りで焼肉'
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
    
    elif message.content.startswith('ぼれろ、こんだて'):
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

    elif message.content.startswith('ぼれろ〜'):
        if len(message.content.strip()) == 4:
            commonreply = ['どうしました〜？','なぁに〜？','ん〜？','とってもすごいBoleroです！']
            random_commonreply = random.choice(commonreply)
            await message.channel.send(f'{random_commonreply}')
        elif len(message.content) > 4:
            agreement =['うんうん','たしかに','そっか','知らなかった','すごく','はい','えっとね','えっ','へぇ〜','なんと','でも','まじか','わっ']
            letter = ['おなかすいたね','のどかわいたね','ねむいね','おはようの時間だね','いいね','おやすみの時間だね','ナントの勅令だよ','土砂降りだ','おばけかも','かっこいい','とても晴れてるよ']
            random_agreement = random.choice(agreement)
            random_letter = random.choice(letter)
            await message.channel.send(f'{random_agreement}、{random_letter}〜。')

    elif message.content.startswith('ぼれろ、えもじ'):
        animal_emojis = [
            '🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼', '🐨', '🐯',
            '🦁', '🐮', '🐷', '🐸', '🐵', '🐒', '🐔', '🐧', '🦅', '🦉',
            '🐴', '🦄', '🐺', '🐗', '🐘', '🦏', '🦌', '🐊', '🐉', '🦖',
            '🦕', '🐢', '🐍', '🐙', '🐠', '🐳', '🐝', '🐞', '🐦‍🔥', '🐌'
        ]
        random_emoji = random.choice(animal_emojis)
        await message.add_reaction(random_emoji)

    elif message.content.strip().endswith('か？'):
        questionagree = ['うん、','えっ','う〜ん','ん〜']
        questionletter = ['違うかも〜','そうかも〜','違うよ〜','そうだよ〜']
        random_questionagree = random.choice(questionagree)
        random_questionletter = random.choice(questionletter)
        await message.channel.send(f'{random_questionagree}{random_questionletter}。')

    # リアクション機能は独立したif文のままでOK
    if 'たの' in message.content or 'タノ' in message.content or '頼ん' in message.content or '田野' in message.content or '頼もしい' in message.content or '頼み' in message.content or 'TANO' in message.content or '楽しい' in message.content or '楽しみ' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
client.run(TOKEN)
