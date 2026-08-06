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
        "Xin chào! Bạn cần gì ở tôi."
    )


# Bot đọc tin nhắn và trả lời
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text.lower() == "buff like":
        reply = "Hiện tại tôi không thể hay đợi anh Long Nhật tạo ra"

    elif text.lower() == "Vua":
        reply = "Long Nhật"

    elif "danh sách" in text.lower():
        reply = " 100 like ; 200 like "

    else:
        reply = f"Bạn vừa nói: {text}"


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
