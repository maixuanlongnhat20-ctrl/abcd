import asyncio

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8648003150:AAGBzl-ZccCrXDrGHAkvzt7uj24A4RAS3rQ"


# Khi người dùng bấm /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chào Bố Nhật."
    )


# Bot đọc tin nhắn và trả lời
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text.lower() == "name":
        reply = "Mai Xuân Long Nhật"

    elif text.lower() == "alo":
        reply = "chưa cài đặt"

    elif text.lower() == "xnhau":
        reply = " https://xnhau.tech "

    else:
        reply = f"Tôi không hiểu"


    await update.message.reply_text(reply)



async def main():

    app = Application.builder().token(TOKEN).build()


    # Lệnh /start
    app.add_handler(CommandHandler("start", start))


    # Nhận tất cả tin nhắn văn bản
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
    )


    await app.initialize()
    await app.start()

    await app.updater.start_polling()

    print("Bot đang chạy...")


    await asyncio.Event().wait()



if __name__ == "__main__":
    asyncio.run(main())
