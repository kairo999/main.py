import logging
import random
from telegram import Poll
from telegram.ext import Updater, CommandHandler, CallbackContext, JobQueue
import os

TOKEN = os.getenv("7691172379:AAFH-jvRpv8lJ5nzbZM4-gE5QrsFc8QsgFQ")

QUIZZES = [
    {
        "question": "Which is the largest ocean?",
        "options": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "correct_option": 1
    },
    {
        "question": "Who wrote Romeo and Juliet?",
        "options": ["Shakespeare", "Dickens", "Twain", "Hemingway"],
        "correct_option": 0
    }
]

group_ids = set()
logging.basicConfig(level=logging.INFO)

def send_quiz(context: CallbackContext):
    quiz = random.choice(QUIZZES)
    for chat_id in group_ids:
        context.bot.send_poll(
            chat_id=chat_id,
            question=quiz['question'],
            options=quiz['options'],
            type=Poll.QUIZ,
            correct_option_id=quiz['correct_option']
        )

def start(update, context):
    chat_id = update.effective_chat.id
    group_ids.add(chat_id)
    update.message.reply_text("✅ Quiz bot activated!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    job_queue: JobQueue = updater.job_queue
    job_queue.run_repeating(send_quiz, interval=3600, first=10)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
