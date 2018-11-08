from flask import Flask
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def time():
    now = datetime.now(timezone('America/Mexico_City'))
    return "The current date and time in Mexico City is {}".format(now)

@app.route("/show/<number>")
def show(number):
    return "You passed in {}".format(number)

if __name__ == '__main__':
    app.run(port=5050)