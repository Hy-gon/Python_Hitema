from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# TP1 Flask

# 1.1 - Quickstart

# @app.route("/")
# def index():
#     return "Hello H3"

# Version without template

# @app.route("/ma_route/<name>", methods=["GET"])
# def get_name(name):
#     return "Hello "+name

# Version with template

# @app.route("/ma_route/<name>", methods=["GET"])
# def get_name(name):
#     return render_template("index.htm", my_name=name)

# 1.2 - Mini books API

# books = [
#     {
#         'id': 1,
#         'titre': 'un titre',
#     },
#     {
#         'id': 2,
#         'titre': 'un autre titre random',
#     }
# ]

books = json.load(open("../Data/books.json"))


@app.route("/")
def index():
    return "Hello my app"


@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)


# @app.route("/api/book/<int:id>", methods=["GET"])
# def get_book(id):
#     book = None
#     for val in books:
#         if val.get("id") == id:
#             book = val
#             break
#     return jsonify(book)

@app.route("/api/book/<string:title>", methods=["GET"])
def get_book_by_title(title):
    book = None
    for val in books:
        if val.get("title") == title:
            book = val
            break
    # return jsonify(book)
    return render_template("book_by_title.htm", book=book)


if __name__ == "__main__":
    app.run(debug=True)
