from flask import Flask
import json

app = Flask(__name__)

# TP1 Flask

# 1.1 - Quickstart

@app.route('/')
def index():
    return "Hello H3"

if __name__ == "__main__":
    app.run(debug=True)
