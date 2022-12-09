import constantes as keys
# importa a extensao para bot do telegram
# nao esquecer de dar source no env e instalar a extensao com o pip
from telegram.ext import *
import main as M

print("Bot iniciado.")

def start_command(update, context):
    update.message.reply_text('digite algo para iniciar o bot')

def help_command(update, context):
    update.message.reply_text('se precisar de ajuda procura no google')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = M.pega_resposta(text).replace("<br>", "\n")

    update.message.reply_text(response)

def error(update, context):
    print(f"update {update} causou o erro {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("start", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()