from flask import Flask, render_template

app = Flask(__name__)

texts = ["¡Hola mundo!", "Hello world!", "Bonjour le monde!"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/Español")
def Español():
    return texts[0]


@app.route("/English")
def English():
    return texts[1]


@app.route("/Français")
def Français():
    return texts[2]


if __name__ == '__main__':
    app.run()
