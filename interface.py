from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import sqlite3
import prettytable

updater = Updater(token='387336652:AAGjsmACpRkfJcaMyV5rsPujcdiGfcyGcf0')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dispatcher = updater.dispatcher


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a bot, please talk to me!")

def points(bot, update):
    table = []
    conn = sqlite3.connect('points.db')
    c = conn.cursor()
    # Add in prettytable
    table = prettytable.PrettyTable(
        ['Manager','StatusOfPlayer'])
    points = c.execute('SELECT * from LatestPoints')
    for el in points:
		table.add_row(el)
    bot.sendMessage(chat_id=update.message.chat_id, text=str(table))

def whohas(bot,update,args):
    table=[]
    conn=sqlite3.connect('points.db')
    c = conn.cursor()
    # Add in prettytable
    table = prettytable.PrettyTable(
        ['Manager','Points'])
    points = c.execute('Select ManagerName,statusOfPlayer from playerInfo WHERE playerName LIKE ?',['%'+args[0]+'%'])

    for el in points:
        table.add_row(el)
    bot.sendMessage(chat_id=update.message.chat_id, text=str(table))

def captains(bot,update):
    table=[]
    conn=sqlite3.connect('points.db')
    c = conn.cursor()
    # Add in prettytable
    table = prettytable.PrettyTable(
        ['Player','Manager'])
    points = c.execute('SELECT PlayerName,ManagerName from playerInfo where PlayerTitle="Captain"')
    for el in points:
        table.add_row(el)
    bot.sendMessage(chat_id=update.message.chat_id, text=str(table))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

iplPoints_handler = CommandHandler('points', points)
dispatcher.add_handler(iplPoints_handler)

whohas_handler = CommandHandler('whohas', whohas, pass_args=True)
dispatcher.add_handler(whohas_handler)

captains_handler = CommandHandler('captains', captains)
dispatcher.add_handler(captains_handler)


updater.start_polling()
