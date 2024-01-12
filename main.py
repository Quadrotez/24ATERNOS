from configparser import ConfigParser
from javascript import require, On

mineflayer = require('mineflayer')
import threading, os
from sys import platform

### By Fortcote
### https://discord.gg/bjgpVAxgyE

config = ConfigParser()
config.read('config.ini')


def started(stop):
    bot = mineflayer.createBot({
        'host': config.get('server', 'host'),
        'port': config.get('server', 'port'),
        'username': config.get('bot', 'name')})

    @On(bot, "error")
    def error(err, *a):
        print("Connect ERROR: ", err, a)

    @On(bot, "kicked")
    def kicked(this, reason, *a):
        print("I was kicked: ", reason, a)
        print('reconnect')
        bot.end();
        bot.join()

    @On(bot, "chat")
    def handle(this, username, message, *args):
        if username == bot.username:
            return
        elif message.startswith(config.get('command', 'position')):
            p = bot.entity.position;
            bot.chat(f"Bot > I am at {p.toString()}")
        elif message.startswith(config.get('command', 'start')):
            bot.chat('24 ATERNOS > Bot started! - Made By Fortcote')
            bot.setControlState('forward', True)
            bot.setControlState('jump', True)
            bot.setControlState('sprint', True)
        elif message.startswith(config.get('command', 'stop')):
            bot.chat('24 ATERNOS > Bot stoped! - Made By Fortcote')
            bot.clearControlStates()

    @On(bot, "spawn")
    def spawn(this):
        bot.chat("Bot > Spawned!")

    @On(bot, "death")
    def death(this):
        bot.chat("Bot > Respawn!")


def start():
    global bott, stop_threads
    stop_threads = False
    bott = threading.Thread(target=started, args=(lambda: stop_threads,))
    bott.start()


def stop():
    try:
        if platform == "win32":
            os.system('taskkill /f /im node.exe')
        else:
            os.system('killall node')
    except:
        pass




while True:
    func = input('Введите функцию: ')


    if func == 'start':
        print('Начало работы...')
        start()