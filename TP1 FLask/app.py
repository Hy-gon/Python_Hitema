from flask import Flask, render_template
import json

app = Flask(__name__)

# TP1 Flask

# 1.1 - Quickstart

#@app.route('/')
#def index():
#    return "Hello H3"

# Without Index Template

#@app.route("/routeName/<name>", methods=["GET"])
#def get_name(name):
#    return "Hello " + name

# With Index Template

#@app.route("/routeNametest/<name>", methods=["GET"])
#def get_name(name):
#    return render_template("index.html", name = name)

book = [
    {
        'id': 1,
        'title': 'titre 1',
    },
    {
        'id': 2,
        'title': 'titre 2',
    }
]

@app.route("/")
def index():
    return render_template('index.html')

# ID book
@app.route("api/books/<int:id>", methods=["GET"])
def get_books_id():
    pass

# TITLE book
@app.route("api/books/<title>", methods=["GET"])
def get_books_title():
    pass

# book list
@app.route("/api/books", methods["GET"])
def books():
    return render_template('books.html')






if __name__ == "__main__":
    app.run(debug=True)