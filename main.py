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
    await client.change_presence(activity=discord.Game(name="自転車練習動画"))

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
        await message.channel.send(f'{message.author.display_name}ちゃんのおこづかいはね、 {currency[user_id]} ターノだよ〜。')

    elif message.content.startswith('ぼれろ、おこづかい'):
        cooldown_time = 86400
        
        if user_id in last_earn_times and (time.time() - last_earn_times[user_id] < cooldown_time):
            remaining_time = int(cooldown_time - (time.time() - last_earn_times[user_id]))
            await message.channel.send(f'{message.author.display_name}ちゃん、もうもらったでしょ〜')
        else:
            earned = random.randint(200, 400)
            currency[user_id] += earned
            last_earn_times[user_id] = time.time()
            save_currency(currency)
            await message.channel.send(f'{message.author.display_name}ちゃんに {earned} ターノあげる〜！')

    elif message.content == 'ぼれろ、おつかい':
        # 消費する金額を180に固定
        amount_to_spend = 180
        
        try:
            # 残高が十分かチェック
            if currency[user_id] >= amount_to_spend:
                currency[user_id] -= amount_to_spend
                save_currency(currency)
                items = [
                    '【C】カルパス', '【C】ソーダ', '【C】お茶', '【C】シーグラス', '【C】えんぴつ',
                    '【C】トマト', '【C】しゃこパン', '【C】付箋', '【C】おにぎり', '【C】にんじん',
                    '【C】じゃがいも', '【UC】グミ', '【UC】コーラ', '【UC】消しゴム', '【UC】チョコレート',
                    '【UC】かぼちゃ', '【UC】ヨーヨー', '【UC】メロンパン', '【UC】メロンソーダ',
                    '【UC】ハンカチ', '【R】マグカップ', '【R】ミニチュアフィギュア', '【R】メンチカツ',
                    '【R】フェイスタオル', '【R】クリアボトル', '【R】ライト', '【SR】クッション',
                    '【SR】お布団', '【SR】ぬいぐるみ', '【SR】スーツ', '【SR】まくら',
                    '【HR】マグロ', '【HR】マツタケ', '【HR】和牛', '【UR】月の土地'
                ]
                weights = [100,100,100,100,100,100,100,100,100,100,90,90,90,90,90,90,90,90,90,70,70,70,70,70,70,40,40,40,40,40,25,25,25,3]
                pulled_item = random.choices(items, weights=weights, k=1)[0]
                await message.channel.send(f'{message.author.display_name}ちゃんからもらった{amount_to_spend} ターノで {pulled_item} を買ってきたよ〜！')
            else:
                await message.channel.send(f'{message.author.display_name}ちゃんのターノだと買えないかも......!')
        except Exception as e:
            # エラーが発生した場合にエラー内容を表示
            await message.channel.send(f'ごめんね、おつかい中にエラーが発生したみたい: `{e}`')

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

    if 'たの' in message.content or 'タノ' in message.content or '頼ん' in message.content or '田野' in message.content or '頼もしい' in message.content or '頼み' in message.content or 'TANO' in message.content or '楽しい' in message.content or '楽しみ' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
client.run(TOKEN)
