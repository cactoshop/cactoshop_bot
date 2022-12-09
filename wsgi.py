from app.main import app
import telegram_bot_integration
import multiprocessing

if __name__ == '__main__':
     webapp_proc = multiprocessing.Process(name='webapp_proc', target=app.run)
     telegram_proc = multiprocessing.Process(name='telegram_proc', target=telegram_bot_integration.main)
     telegram_proc.start()
     webapp_proc.start()