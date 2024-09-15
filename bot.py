from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.error import TelegramError

# Replace with your bot token
BOT_TOKEN = '7254519456:AAE3NCXWVjJd-CS-oJWgnY0AwP4sd6ftEmY'
# Replace with your chat ID if needed; otherwise, the bot will respond to messages it receives

IMAGE_URL_TGM = 'https://example.com/image_tgm.jpg'
IMAGE_URL_GRAF = 'https://example.com/image_graf.jpg'

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! Use /tgm or /graf to get image links.")

def send_image_tgm(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    try:
        context.bot.send_message(
            chat_id=chat_id,
            text=f"Here is the TGM image: [Image Link]({IMAGE_URL_TGM})",
            parse_mode='Markdown'
        )
    except TelegramError as e:
        print(f"An error occurred: {e}")

def send_image_graf(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    try:
        context.bot.send_message(
            chat_id=chat_id,
            text=f"Here is the GRAF image: [Image Link]({IMAGE_URL_GRAF})",
            parse_mode='Markdown'
        )
    except TelegramError as e:
        print(f"An error occurred: {e}")

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('tgm', send_image_tgm))
    dispatcher.add_handler(CommandHandler('graf', send_image_graf))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()