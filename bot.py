import logging
import traceback
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
# =====================
# CẤU HÌNH
# =====================
TOKEN = "8648003150:AAGBzl-ZccCrXDrGHAkvzt7uj24A4RAS3rQ"
OWNER_ID = 6821471310
# =====================
# LOG
# =====================
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
# =====================
# XỬ LÝ LỖI
# =====================
async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(
        "Bot gặp lỗi:",
        exc_info=context.error
    )
    traceback.print_exception(
        type(context.error),
        context.error,
        context.error.__traceback__
    )
# =====================
# CÁC LỆNH
# =====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Chào bạn 👻\n"
        "Bot đang hoạt động bình thường.\n\n"
        "Gõ /help để xem lệnh."
    )
async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Admin: Long Nhật"
    )
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 ID Telegram của bạn:\n{update.effective_user.id}"
    )
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 DANH SÁCH LỆNH\n\n"
        "/start - Khởi động bot\n"
        "/admin - Thông tin admin\n"
        "/get_id - Lấy ID Telegram\n"
        "/help - Danh sách lệnh\n"
        "/stop - Tắt bot (chỉ admin)\n"
        "/restart - Khởi động lại bot (chỉ admin)"
    )
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text(
            "❌ Bạn không có quyền dùng lệnh này."
        )
        return
    await update.message.reply_text(
        "🛑 Bot đang tắt..."
    )
    await context.application.stop()
async def restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text(
            "❌ Bạn không có quyền dùng lệnh này."
        )
        return
    await update.message.reply_text(
        "🔄 Bot đang khởi động lại..."
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
    # Lệnh
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CommandHandler("get_id", get_id))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("restart", restart))
    # Bắt lỗi
    app.add_error_handler(error_handler)
    logger.info("🤖 Bot đang chạy...")
    app.run_polling(
        drop_pending_updates=True
    )
if __name__ == "__main__":
    main()
