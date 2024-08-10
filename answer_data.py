from random import choice
from datetime import datetime

def find_answer(answer):

    now = datetime.now()

    data = {
        "hello" : [
        'Привет бро!🤜🤛', 'Здарова', 'Хаю хай!'
        ],
        "hi" : [
        'Привет кукушка🤟'
        ],
        "ever" : [
        'Привет, {0.author}!', 'Ку, {0.author}!', 'Здаров, {0.author}!', 'Приветствую, {0.author}!'
        ],
        "progg" : [
        'Ладненько)', 'Окей)', 'Та без Б бро)'
        ],
        "dis_cor" : [
        'https://discord.gg/zMGhgC'
        ],
        "mine" : [
        'dan2215t.aternos.me'
        ],
        "gg" : [
        '🎮', 'Истинно так)'
        ],
        "what" : [
        'У меня как у бота 😎 \n Если ты меня спросил 🙂'
        ],
        "canal" : [
        'https://www.youtube.com/channel/UCiNdgVUWYsTzaVdlISnFdiQ'
        ],
        ")" : [
        '🙂'
        ],
        "(" : [
        '🙁'
        ],
        "test" : [
        'Да, {0.author} я тут. Что то случилось?', 'Да, я тут {0.author}.'
        ],
        "crow" : [
        '😎'
        ],
        "nice" : [
        '👍'
        ],
        "timen" : [
        'На сервере сейчас ' + str(now.hour) + ' часов ' + str(now.minute) + ' минут'
        ],
        "date" : [
        "На сервере сегодня " + str(now.year)  + " г. " + str(now.month) + " м. " + str(now.day) + " д. " + str(now.hour) + " ч. " + str(now.minute) + " м. " + str(now.second) + " с."
        ],
        "ly" : [
        'ля ля ля тополя и вам того же мне не ля!'
        ],
        "fun" : [
        'https://tenor.com/view/%D1%81%D0%BC%D0%B5%D1%85-%D0%B4%D0%B5%D0%B4%D1%81%D0%BC%D0%B5%D1%91%D1%82%D1%8C%D1%81%D1%8F-%D1%83%D0%B3%D0%B0%D1%80-%D1%85%D0%B0%D1%85%D0%B0%D1%85%D0%B0%D1%85-%D0%B4%D0%B5%D0%B4%D0%BC%D0%B5%D0%BC-gif-15106228',
        'https://tenor.com/view/laugh-lol-rofl-laughing-ketawa-gif-10164703',
        'https://tenor.com/view/minions-lol-laugh-gif-4519852',
        '😂'
        ],
        "M" : [
        'https://tenor.com/view/hitmans-bodyguard-hitmans-bodyguard-gifs-samuel-ljackson-time-tick-tock-gif-8352665',
        '⏱️'
        ],
        "slip" : [
        '😴'
        ],
        "yes" : [
        'ты забыл √'
        ],
    }

    return choice(data[answer])

    '''
    values = [] #Constantly updated Mass

    for value in data[answer]:
        values.append(value)

    return choice(values)
    '''
