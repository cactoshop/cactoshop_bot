from flask import Flask, render_template, request
import main as M

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    msg = request.form["msg"]
    response = M.pega_resposta(msg)
    return str(response)

if __name__ == '__main__':
    app.run()