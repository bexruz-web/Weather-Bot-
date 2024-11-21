from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from config import TOKEN, ADMIN_ID
from database import Database
from buttons import region_inline_buttons
from get_weather import get_all_regions
from inlines import inline_handler\

db = Database()

def help(update, context):
    update.message.reply_text(text="<i>Bu bot tanlagan shahringizni kunlik yoki 3 kunlik malumotini ko'rsatadi. /start bosing 😇</i>", parse_mode='HTML')

def start(update, context):
    user = update.effective_user
    user_db = db.get_user_by_chat_id(chat_id=user.id)

    if user_db is None:
        db.create_user(
            first_name=user.first_name,
            username=user.username if user.username else "Username yo'q",
            chat_id=user.id
        )
        update.message.reply_text(
            text=f"Salom👋🏻 <b>{user.first_name}</b> Xush kelibsiz\n\n"
                 f"📍 Marhamat kerakli viloyatni tanlang:",
            parse_mode='HTML',
            reply_markup=region_inline_buttons(get_all_regions())
        )

        message = f"Yangi foydalanuvchi qo'shildi:\nID: {user.id}\nIsmi: {user.first_name}\nFoydalanuvchi nomi: @{user.username}"
        for admin_id in ADMIN_ID:
            if user_db is None:
                context.bot.send_message(chat_id=admin_id, text=message)

    else:
        update.message.reply_text(
            text=f"📍 Marhamat kerakli viloyatni tanlang:",
            parse_mode='HTML',
            reply_markup=region_inline_buttons(get_all_regions())
        )

def main():
    print('Bot ishga tushdi....')
    updater = Updater(token=TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CallbackQueryHandler(inline_handler))
    dp.add_handler(MessageHandler(Filters.all, help))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()


