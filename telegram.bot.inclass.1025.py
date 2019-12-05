from telegram.ext import Updater, CommandHandler
from random import sample
from itertools import combinations

# Check whether a input is valid
def valid(s):
    if len(s)!=4:
        return False
    if any(x not in '0123456789' for x in s):
        return False
    if any(x==y for x, y in combinations(s,2)):
        return False
    return True

ans = ''.join(sample('0123456789',4))
print('The answer is',ans)

def new_game(bot, update):
    global ans
    ans = ''.join(sample('0123456789',4))
    print('The answer is',ans)
    update.message.reply_text("OK! Let's start a new game!")

def guess(bot, update):
    toks = update.message.text.strip().split()
    print(toks)
    if len(toks) != 2:
        msg = "Wrong format. It should be like `/guess 1234`."
    elif valid(toks[1]) == False:
        msg = "{} is invalid.".format(toks[1])
    else:
        A = sum(1 for x,y in zip(toks[1],ans) if x==y)
        B = sum(1 for x in toks[1] if x in ans)-A
        result = "{}A{}B".format(A,B)
        msg = "{} is {}".format(toks[1], result)
    update.message.reply_text(msg)
    if msg.endswith('4A0B'): new_game(bot, update)

def hello(bot, update):
    update.message.reply_text(
        'hello, {}'.format(update.message.from_user.first_name))

def bye(bot, update):
    update.message.reply_text(
        '{}, bye!'.format(update.message.from_user.first_name))
    
def show_text(bot, update):
    text = update.message.text
    print('We received:')
    print(text)
    update.message.reply_text(
        'Echo: {}'.format(text))

with open('C:/token.txt') as FILE:
    token = FILE.readline()

updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('bye', bye))
updater.dispatcher.add_handler(CommandHandler('content', show_text))
updater.dispatcher.add_handler(CommandHandler('new', new_game))
updater.dispatcher.add_handler(CommandHandler('guess', guess))

updater.start_polling()
updater.idle()






















