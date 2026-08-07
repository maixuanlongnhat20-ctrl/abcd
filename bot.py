import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# =====================
# CẤU HÌNH
# =====================

TOKEN =  "8648003150:AAGBzlZccCrXDrGHAkvzt7uj24A4RAS3rQ"
OWNER_ID = 6821471310

# =====================
# LOG
# =====================

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# =====================
# CÁC LỆNH BOT
# =====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chào bạn 👻\n"
        "Tôi có thể giúp gì cho bạn?\n\n"
        "Gõ /help để xem danh sách lệnh."
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Admin: Long Nhật"
    )


async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 ID Telegram của bạn là: {update.effective_user.id}"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 DANH SÁCH LỆNH\n\n"
        "/start - Khởi động bot\n"
        "/admin - Thông tin admin\n"
        "/help - Danh sách lệnh\n"
        "/stop - Tắt bot (chỉ admin)"
    )


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Chỉ chủ bot mới được dùng /stop
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text(
            "❌ Bạn không có quyền dùng lệnh này."
        )
        return

    await update.message.reply_text(
        "🛑 Bot đang tắt..."
    )

    await context.application.stop()


# =====================
# CHẠY BOT
# =====================

def main():
    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    # Đăng ký các lệnh
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stop", stop))

    print("🤖 Bot đang chạy...")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
