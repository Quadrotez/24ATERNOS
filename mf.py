from configparser import ConfigParser
import threading, os
from sys import platform
from javascript import require, On
config = ConfigParser()
config.read('config.ini')



mineflayer = require('mineflayer')
bot = None

def started(stop):
    global bot
    bot = mineflayer.createBot({
        'host': config.get('SERVER', 'host'),
        'port': config.get('SERVER', 'port'),
        'username': config.get('BOT', 'name')})

    @On(bot, "error")
    def error(err, *a):
        print("Connect ERROR: ", err, a)

    @On(bot, "kicked")
    def kicked(this, reason, *a):
        print("I was kicked: ", reason, a)
        print('reconnect')
        bot.end()
        bot.join()

    @On(bot, "chat")
    def handle(this, username, message, *args):
        if username == bot.username:
            return
        elif message.startswith(config.get('COMMAND', 'position')):
            p = bot.entity.position;
            bot.chat(f"Bot > I am at {p.toString()}")
        elif message.startswith(config.get('COMMAND', 'start')):
            bot.chat('Bot started!')
            bot.setControlState('forward', True)
            bot.setControlState('jump', True)
            bot.setControlState('sprint', True)
        elif message.startswith(config.get('COMMAND', 'stop')):
            bot.chat('Я ухожу')
            bot.clearControlStates()

    @On(bot, "spawn")
    def spawn(this):
        bot.chat("Spawned!")

    @On(bot, "death")
    def death(this):
        bot.chat("Respawn!")


def start():
    global bott, stop_threads
    stop_threads = False
    bott = threading.Thread(target=started, args=(lambda: stop_threads,))
    bott.start()


def stop9():
    try:
        if platform == "win32":
            os.system('taskkill /f /im node.exe')
        else:
            os.system('killall node')
    except:
        pass

def stop():
    global bot
    bot.end()
