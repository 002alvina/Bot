from typing import Final
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Application

import logging
TOKEN:Final = "6345119679:AAEJv0lD38kO8vNhDGIjovYprnsrrUgs9uY"
BOT_USERNAME: Final = '@sss_hhh_ooo_ppp'
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a command handler for the /start command
async def start(update: Update, context: CallbackContext) -> None:
    # Define the custom keyboard layout
    keyboard = [
        [KeyboardButton(text="Каталог")],
        [KeyboardButton(text="Поиск"), KeyboardButton(text="Отзывы")],
        [KeyboardButton(text="Поддержка")],
        [KeyboardButton(text="Мои заказы"), KeyboardButton(text="Корзина")]
    ]
    
    # Create a ReplyKeyboardMarkup object with the keyboard layout
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    
    # Send the welcome message with the custom keyboard
    welcome_text = (
        "Здравствуйте!\n\n"
        "Бот представляет полный ассортимент кроссовок магазина Sneaker Club. "
        "Чтобы оформить заказ, пожалуйста, перейдите в «Каталог», выберите нужную модель "
        "кроссовок и укажите данные покупателя. После этого ожидайте сообщение от "
        "менеджера для подтверждения заказа.\n\n"
        "По заказам и вопросам, пишите в специальный бот по кнопке «Поддержка»."
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# Define a command handler for the other commands to respond with a placeholder text
def handle_message(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Команда еще не реализована.")

# Define an error handler
def error_handler(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

# Main function where the bot is initialized
def main() -> None:
    # Create the Updater and pass it your bot's token
  app = Application.builder().token(TOKEN).build()

    # Get the dispatcher to register handlers
    
    # Register the command handlers
  app.add_handler(CommandHandler("start", start))
    
    # Register the error handler
  app.add_error_handler(error_handler)

    # Start the Bot
  print("Poling...")
  app.run_polling(poll_interval=3)

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
  app.idle()

if __name__ == '__main__':
    main()
