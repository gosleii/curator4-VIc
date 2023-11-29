import telebot

bot = telebot.TeleBot('6879940916:AAE9xTz4GP2fmGNGfTxXfFls4DjFDi2oHgs')


@bot.message_handler(comande=['start'])
def main(messege):
    bot.send_message(messege.chat.id, 'Wnat?')


@bot.message_handler(comande=['joke'])
def main(messege):
    bot.send_message(messege.chat.id, 'No joke \nThis is true!')


@bot.message_handler(comande=['mes?'])
def main(messege):
    bot.send_message(messege.chat.id, '*TG*\n_TG_', parse_mode = 'Markdown')

@bot.message_handler(comande=['mess?'])
def main(messege):
    bot.send_message(messege.chat.id, '[Жамкай!](https://ru.wikipedia.org/wiki/Заглавная_страница)', parse_mode = 'Markdown')

bot.infinity_polling()