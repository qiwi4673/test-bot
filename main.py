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
    await client.change_presence(activity=discord.Game(name="お人形遊び"))

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

    elif message.content.startswith('ぼれろ、うんだめし'):
        cooldown_time = 600
        
        if user_id in last_earn_times and (time.time() - last_earn_times[user_id] < cooldown_time):
            remaining_time = int(cooldown_time - (time.time() - last_earn_times[user_id]))
            await message.reply(f'10分に1回占うよ〜')
        else:
            earned = random.randint(200, 400)
            currency[user_id] += earned
            last_earn_times[user_id] = time.time()
            save_currency(currency)
            luck_lank = ['いい感じ','好調','絶好調','やや悪']
            luck_msga = ['隣の人が' ,'近くのものが','足の小指が','目の前で','おとといの夜ごはんが','朝起きた時に','料理中に','お散歩中に']
            luck_msgb = ['はんぺんになる','土に埋まる','見つかる','食べられる','溶ける','光る','強くなる','将棋をする']
            lc = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',]
            rnd_luck_lank = random.choice(luck_lank)
            rnd_luck_msga = random.choice(luck_msga)
            rnd_luck_msgb = random.choice(luck_msgb)
            rnd_lca = random.choice(lc)
            rnd_lcb = random.choice(lc)
            rnd_lcc = random.choice(lc)
            rnd_lcd = random.choice(lc)
            rnd_lce = random.choice(lc)
            rnd_lcf = random.choice(lc)
            await message.reply(f'{message.author.display_name}ちゃんの今の運勢は〜 \n{rnd_luck_lank}で{rnd_luck_msga}{rnd_luck_msgb}かも〜 \nラッキーカラーは#{rnd_lca}{rnd_lcb}{rnd_lcc}{rnd_lcd}{rnd_lce}{rnd_lcf}だよ〜！')

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
                weights = [100,100,100,100,100,100,100,100,100,100,100,90,90,90,90,90,90,90,90,90,70,70,70,70,70,70,40,40,40,40,40,25,25,25,3]
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

    elif message.content.startswith('10連コンコンガチャ'):
        roushi = ['★☆☆懇浪','★☆☆コンコン','★☆☆浪士','★☆☆ン浪','★☆☆ろーし','★☆☆:gotume~kawauso:','★☆☆ヤクザ','★☆☆きつねうどん','★☆☆うどんきつね','★☆☆おあげ','★☆☆キツネ','★★☆コンコン浪士','★★☆懇々浪士','★★☆組長','★★☆コンコン浪士"メイド服"','★★☆コンコン浪士"チーパオ"','★★☆コンコン浪士"ディアンドル"','★★☆伝説の名前','★★☆著名な祖父を持ちし孫','★★★★★ろうてゃ','★★★コンコン老人','★★★★士浪ンコンコ',]
        roushiweight = [100,100,100,100,100,100,100,100,100,100,100,15,15,15,15,15,15,15,15,1,5,3]
        
        # random.choicesを使って、リストから10個のアイテムを重み付けに基づいて選択
        pulled_items = random.choices(roushi, weights=roushiweight, k=10)
        
        # 結果をまとめて一つの文字列にする
        result_message = '\n'.join(pulled_items)
        
        await message.reply(f'10連ガチャだよ〜！\n\n{result_message} \nいいのでたかな？')

    elif message.content.startswith('100連コンコンガチャ'):
        rousi = ['★☆☆懇浪','★☆☆コンコン','★☆☆浪士','★☆☆ン浪','★☆☆ろーし','★☆☆:gotume~kawauso:','★☆☆ヤクザ','★☆☆きつねうどん','★☆☆うどんきつね','★☆☆おあげ','★☆☆キツネ','★★☆コンコン浪士','★★☆懇々浪士','★★☆組長','★★☆コンコン浪士"メイド服"','★★☆コンコン浪士"チーパオ"','★★☆コンコン浪士"ディアンドル"','★★☆伝説の名前','★★☆著名な祖父を持ちし孫','★★★★★ろうてゃ','★★★コンコン老人','★★★★士浪ンコンコ',]
        rousiweight = [1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,10,10,10,10,10,10,10,10,1,3,2]
        
        # random.choicesを使って、リストから10個のアイテムを重み付けに基づいて選択
        pull_rousi = random.choices(rousi, weights=rousiweight, k=100)
        
        # 結果をまとめて一つの文字列にする
        result_rousi = '\n'.join(pull_rousi)
        
        await message.reply(f'100連ガチャだよ〜！\n\n{result_rousi} \nいいのでたかな？')
        
    elif message.content.strip().endswith('かな？'):
        questionagree = ['うん、','えっ','う〜ん','ん〜','もしかしたら']
        questionletter = ['違うかも〜','そうかも〜','もしかするかも〜']
        random_questionagree = random.choice(questionagree)
        random_questionletter = random.choice(questionletter)
        await message.channel.send(f'{random_questionagree}{random_questionletter}。')
    
    if 'たの' in message.content or 'タノ' in message.content or '頼ん' in message.content or '豚の' in message.content or '歌の' in message.content or '肩の' in message.content or '多能' in message.content or '多脳' in message.content or '板野' in message.content or '愉しい' in message.content or '愉しみ' in message.content or '愉しむ' in message.content or '愉しま' in message.content or '愉しも' in message.content or '愉しめ' in message.content or ':gotsume_kawauso:' in message.content or ':gotsume_kawauso~1:' in message.content or '頼ま' in message.content or '田野' in message.content or '頼もしい' in message.content or '頼み' in message.content or 'TANO' in message.content or 'tano' in message.content or '北野' in message.content or '北の' in message.content or '頼め' in message.content or '頼む' in message.content or '頼もう' in message.content or '楽しい' in message.content or '楽しみ' in message.content or 't4no' in message.content or 't4n0' in message.content or '7ano' in message.content:
        custom_emoji = client.get_emoji(1415213398546714704)
        if custom_emoji:
            await message.add_reaction(custom_emoji)

TOKEN = os.getenv("DISCORD_TOKEN")
keep_alive()
client.run(TOKEN)
