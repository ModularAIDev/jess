from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Bot
from dotenv import load_dotenv
from telegram_client import send_message
from jess.crew import create_crew_for_question
import os

load_dotenv()

chat_id = os.getenv('TELEGRAM_CHAT_ID')
telegram_token = os.getenv('TELEGRAM_TOKEN')


async def start(update, context):
    if str(update.message.chat_id) != str(chat_id):
        return
    await update.message.reply_text('One sec, warming up.')


async def message(update, context):
    if update and update.message and str(update.message.chat_id) != str(chat_id):
        return
    answer = create_crew_for_question(update.message.text).kickoff()
    await update.message.reply_text(answer)
    # send_message(chat_id, answer)


async def get_chat_id(update, context):
    chat_id = update.message.chat_id
    await update.message.reply_text(f"Your chat ID is: {chat_id}")


bot = Bot(token=telegram_token)


def main():
    print("starting")
    application = Application.builder().bot(bot).build()
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    get_chat_id_handler = CommandHandler('get_chat_id', get_chat_id)
    application.add_handler(get_chat_id_handler)    

    main_handler = MessageHandler(filters.TEXT, message)
    application.add_handler(main_handler)

    application.run_polling()


if __name__ == '__main__':
    main()