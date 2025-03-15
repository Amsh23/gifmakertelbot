import os
import asyncio
from dotenv import load_dotenv  # type: ignore
from PIL import Image  # type: ignore
from telegram import Update  # type: ignore
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes  # type: ignore
from telegram.error import TimedOut, NetworkError  # type: ignore

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# پوشه ذخیره‌سازی عکس‌ها
IMAGE_FOLDER = "images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

# دریافت توکن از محیط (باید در فایل .env ذخیره شده باشد)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # توکن را از متغیر محیطی TELEGRAM_BOT_TOKEN می‌خوانیم

# تنظیمات تایم‌اوت برای درخواست‌ها
CONNECT_TIMEOUT = 60  # تایم‌اوت اتصال (ثانیه)
READ_TIMEOUT = 120    # تایم‌اوت خواندن (ثانیه)

# دستور شروع برای ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام! عکس‌های خود را ارسال کنید تا گیف بسازم.")

# ذخیره کردن عکس‌ها
async def save_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message.photo:
        return

    try:
        file = await update.message.photo[-1].get_file()  # دریافت آخرین عکس
        image_path = os.path.join(IMAGE_FOLDER, f"{update.message.from_user.id}_{file.file_id}.jpg")
        await file.download_to_drive(image_path)

        await update.message.reply_text("✅ عکس ذخیره شد! عکس‌های بیشتری ارسال کنید یا از /makegif برای ساخت گیف استفاده کنید.")

    except (TimedOut, NetworkError) as e:
        # زمان‌بندی درخواست تمام شده یا خطای شبکه
        await update.message.reply_text(f"⚠️ خطای شبکه: {e}")

    except Exception as e:
        # مدیریت سایر خطاها
        await update.message.reply_text(f"⚠️ خطا: {e}")

# ساخت گیف از عکس‌ها
async def make_gif(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.message.from_user.id)
    image_files = sorted(
        [os.path.join(IMAGE_FOLDER, f) for f in os.listdir(IMAGE_FOLDER) if f.startswith(user_id)]
    )

    if len(image_files) < 2:
        await update.message.reply_text("❌ حداقل دو عکس ارسال کنید!")
        return

    gif_path = os.path.join(IMAGE_FOLDER, f"{user_id}_animated.gif")
    
    try:
        images = [Image.open(img) for img in image_files]

        # ساخت گیف
        images[0].save(
            gif_path,
            save_all=True,
            append_images=images[1:],
            duration=500,  # مدت زمان هر فریم (میلی‌ثانیه)
            loop=0
        )

        # ارسال گیف به کاربر
        with open(gif_path, "rb") as gif:
            await update.message.reply_animation(gif)

    except Exception as e:
        await update.message.reply_text(f"⚠️ خطایی رخ داد: {e}")

    finally:
        # حذف فایل‌ها پس از ارسال
        try:
            for file in image_files:
                os.remove(file)
            os.remove(gif_path)
        except Exception as e:
            print(f"خطا در حذف فایل‌ها: {e}")

# راه‌اندازی ربات
def main():
    if not TOKEN:
        print("⚠️ خطا: توکن ربات تنظیم نشده است!")
        return

    # تنظیم تایم‌اوت اتصال و خواندن
    application = Application.builder().token(TOKEN).connect_timeout(CONNECT_TIMEOUT).read_timeout(READ_TIMEOUT).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("makegif", make_gif))
    application.add_handler(MessageHandler(filters.PHOTO, save_image))

    print("✅ Bot is running...")
    application.run_polling()

# اطمینان از اجرای صحیح کد
if __name__ == "__main__":
    main()
