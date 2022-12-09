from flask import Flask, render_template, request
import main as M
import telegram_bot_integration
import multiprocessing

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = M.pega_resposta(msg)
    return str(response)

# if __name__ == '__main__':
#     app.run()

if __name__ == '__main__':
     webapp_proc = multiprocessing.Process(name='webapp_proc', target=app.run)
     telegram_proc = multiprocessing.Process(name='telegram_proc', target=telegram_bot_integration.main)
     telegram_proc.start()
     webapp_proc.start()