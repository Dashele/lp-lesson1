from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(massage)s',
	level = logging.INFO,
	filename='bot.log'
	)

def greet_user(bot, update):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text)

def talk_to_me(bot, update):
		user_text = update.message.text
		print(logging.info(user_text))
		update.message.reply_text(user_text)

def main():
	updater = Updater('509973304:AAHQBX-5EgWh0yKCwwOf4YkdB-cHonfnBh4')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	updater.start_polling()
	updater.idle()

main()

