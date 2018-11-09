from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

WORDS = []
with open("large","r") as file:
    for line in file.readlines():
        WORDS.append(line.rstrip())

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/jquery")
def index2():
    return render_template("index2.html")

@app.route("/search")
def search():
    words = [word for word in WORDS if word.startswith(request.args.get("q").lower())]
    return render_template("search.html", words=words)

@app.route("/search2")
def search2():
    words = [word for word in WORDS if word.startswith(request.args.get("q").lower())]
    return jsonify(words)

if __name__ == "__main__":
    app.run(port=5959)

