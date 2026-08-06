import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = "8648003150:AAGBzl-ZccCrXDrGHAkvzt7uj24A4RAS3rQ"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Xin chào! Bot Telegram đã hoạt động 🤖"
    )


async def main():
    app = Application.builder().token(TOKEN).build()

    # thêm lệnh /start
    app.add_handler(CommandHandler("start", start))

    await app.initialize()
    await app.start()

    await app.updater.start_polling()

    print("Bot đang chạy...")

    try:
        await asyncio.Event().wait()
    finally:
        await app.updater.stop()
        await app.stop()
        await app.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
