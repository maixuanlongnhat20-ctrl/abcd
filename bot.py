from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN ="8648003150:AAEM--pLAj2HymExV2_dqe6W1_PhJxHAonk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Xin chào! Bot Telegram đã hoạt động 🤖"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
