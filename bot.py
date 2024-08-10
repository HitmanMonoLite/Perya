#import discord
import input_data
import answer_data
import time
import random
import datetime
import os
import random
import keyboard
from discord import Intents, Client, Game, Status
from discord.ext.commands import Bot
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

#keyboard.press_and_release('alt+Enter')

#PREFIX = ("$")
bot = commands.Bot(command_prefix='$', intents=Intents.all())


class MyClient(Client):
    async def on_ready(self):
        channel_2 = bot.get_channel(749213741245136938)
        channel_4 = bot.get_channel(749229576332247060)
        activity  = Game(name = "Red Dead Redemption 2", type = 3)
        await bot.change_presence(status = Status.online, activity = activity)
        await channel_2.send('@here Привет сервер!')
        #await channel_2.send('@ΉɪȽṃḁղ_ṃʘղʘ_lɪȽҽ#5770 Hello bro!')
        #keyboard.press_and_release('Win+down')
        time.sleep(0.8)
        os.system('cls')
        await channel_4.send('Система активна')
        print("bot started")

    async def on_message(self, message):
        if message.author == self.user:
            print('КАНАЛ:  {0.channel}  |  BOT:           |  [ПЕТЯ]  |  СКАЗАЛ:  |  {0.content}'.format(message))
            return

        #("ﷲﷺȵӛṰŘ﷼ﷻ  ♫#7902" not in str(message.author))
        else:
            print('КАНАЛ:  {0.channel}  |  ПОЛЬЗОВАТЕЛЬ:  |  {0.author}  |  СКАЗАЛ:  |  {0.content}'.format(message))

    # for system

        admin_commands = ["res", "clss", "*", "sp", "Disc_d", "Disc_c", "cd"]

    # system

        request = input_data.find_request(message.content)
        if (request != None):
            if request not in admin_commands:
                #await message.channel.send(request)
                await message.channel.send(answer_data.find_answer(request).format(message))

            # {!for programer!}

            else:
                if '{0.author}'.format(message) == os.getenv('PROGER'):

                    match request:

                        # restart
                        case "res":
                            await message.channel.send('I am restarting this programm')
                            #os.system('start rest.bat')

                        # cls
                        case "clss":
                            await message.channel.send('Командная строка очищена')
                            os.system('cls')

                        # talk of bot
                        case "*":
                            talk = input('Введите, что вы хотите сказать от имени бота: ')
                            await message.channel.send(talk)

                        # spam
                        case "sp":
                            spam = input('Вы действительно хотите заспамить беседу? ')
                            if spam.upper() == 'N':
                                print('Ок, держи в курсе')
                            if spam.upper() == 'Y':
                                await message.channel.send('Ок, ща заспамлю')
                                time.sleep(1)
                                await message.channel.send('ПОДГОТОВКА . . .')
                                time.sleep(5)
                                for i in range(0, 20, 1):
                                    await message.channel.send('ХПХХАхаХАхаХАхахахАХАххаАХХАХАхахАХахХАхАХАХахХАхахахахаахАХхаХАХАхахахаХАХАхахахаХаХаХХАХАхаХАхаах')

                                for i in range(0, 15, 1):
                                    await message.channel.send('https://tenor.com/view/buffy-chair-naughty-spinning-bored-chair-gif-14332549')

                                await message.channel.send('https://tenor.com/view/minionslol-gif-4519852')

                        # disc
                        case "Disc_d":
                            os.system('d:')
                            await message.channel.send('Диск изменён на D')

                        case 'Disc_c':
                            os.system(':c')
                            await message.channel.send('Диск изменён на C')

                        # way
                        case "cd":
                            await message.channel.send('Pleas, print way in command line')
                            way = input('Print way: ')
                            os.system('cd ' + way)
                            await message.channel.send('Path changed on: ' + way)

                else:
                    await message.channel.send('Извините, {0.author} у вас нет прав для данной команды!'.format(message))
                    print('Попатка воспользоваться правами администратора заблокирована')


            """if message.content.startswith('напомни'):
                if (user) == (prog):
                    await message.channel.send('Ок, {0.author} укажите тайминг и ссылку в командной строке'.format(message))
                    timen_1 = input('Тайминг: ')
                    name_s = input('Название: ')
                    link = input('Ссылка: ')
                    while o == True:
                        no_w = datetime.datetime.now()
                        timen_2 = str(no_w.hour) + ':' + str(no_w.minute)
                        if str(timen_1) == str(timen_2):
                            await message.channel.send('Сейчас: ' + timen_1 + ' Стрим на тему: ' + name_s + ' начался по ссылке: ' + link)
                            o = False

                if (user) != (prog):
                    if (prt) != (tr):
                        await message.channel.send('Извините, {0.author} у вас нет прав для данной команды!'.format(message))
                        print('Попатка воспользоваться правами администратора заблокирована')"""

        elif ("cmd " in message.content) and ('{0.author}'.format(message) == os.getenv('PROGER')):
            command = message.content[4:]
            await message.channel.send('Command is: ' + str(command))
            os.system(command)

#Bot set
intents = Intents.default()
intents.message_content = True
bot = MyClient(intents=intents)

# TOKEN
load_dotenv(find_dotenv())
bot.run(os.getenv('TOKEN'))
