from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bitso", methods=["POST"])
def bitso():
    currency = request.form.get("currency")
    res = requests.get(f"https://api.bitso.com/v3/ticker/?book={currency}_mxn")
    if res.status_code != 200:
        return jsonify({"success": False})
    return jsonify(res.json())


if __name__ == '__main__':
    app.run(port=9130, debug=True)
