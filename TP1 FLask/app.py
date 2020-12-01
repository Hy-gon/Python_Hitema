from flask import Flask, render_template
import json

app = Flask(__name__)

# TP1 Flask

# 1.1 - Quickstart

@app.route('/')
def index():
    return "Hello H3"

# Without Index Template

#@app.route("/routeName/<name>", methods=["GET"])
#def get_name(name):
#    return "Hello " + name

# With Index Template

@app.route("/routeNametest/<name>", methods=["GET"])
def get_name(name):
    return render_template("index.html", name = name)



if __name__ == "__main__":
    app.run(debug=True)