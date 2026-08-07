import asyncio
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)


# =====================
# CẤU HÌNH
# =====================

TOKEN = "8648003150:AAGBzl-ZccCrXDrGHAkvzt7uj24A4RAS3rQ"
OWNER_ID = 123456789


# Bật log để dễ sửa lỗi
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


# =====================
# CÁC LỆNH BOT
# =====================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chào bạn 👋\n"
        "Tôi có thể giúp gì cho bạn?"
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Admin: Long Nhật"
    )


async def xsmb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://xoso.com.vn/xo-so-mien-bac/xsmb-p1.html"
    )


async def xnhau(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "https://xnhau.tech"
    )

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"ID Telegram của bạn là: {update.effective_user.id}"
    )
    
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Chỉ chủ bot mới được tắt
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text(
            "Bạn không có quyền dùng lệnh này."
        )
        return

    await update.message.reply_text(
        "Bot đang tắt..."
    )

    await context.application.stop()


# =====================
# CHẠY BOT
# =====================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Danh sách lệnh:\n\n"
        "/start - Khởi động bot\n"
        "/admin - Thông tin admin\n"
        "/xsmb - Xổ số miền Bắc\n"
        "/xnhau - Link Xnhau\n"
        "/help - Danh sách lệnh\n"
        "/stop - Tắt bot (chỉ admin)"
    )
async def main():

    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CommandHandler("xsmb", xsmb))
    app.add_handler(CommandHandler("xnhau", xnhau))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stop", stop))


    print("Bot đang chạy...")


    await app.initialize()
    await app.start()
    await app.updater.start_polling(
        drop_pending_updates=True
    )


    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
