from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('music.db')
        db.row_factory = make_dicts
    return db


@app.route("/")
def index():
    q = request.args.get("q")
    if q:
        rows = get_db().cursor().execute("select a.Title, b.Name from Album a join Artist b on a.ArtistId=b.ArtistId where lower(b.Name) like lower(?)", ('%{}%'.format(q),)).fetchall()
    else:
        rows = get_db().cursor().execute(
            "select a.Title, b.Name from Album a join Artist b on a.ArtistId=b.ArtistId").fetchall()
    return render_template("index.html", rows=rows)


if __name__ == "__main__":
    app.run(port=5959)
