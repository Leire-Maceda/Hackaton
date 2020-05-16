from telegram.ext import Updater, CommandHandler


def main():
    updater =  Updater(token="1289905622:AAHuHtP3Pvc3jTbOu5pbHwhfu9VfJAPdGJM", use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola, soy un bot")
    pass


main()

    
