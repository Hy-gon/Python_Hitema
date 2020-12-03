import sys, os
from flask import Flask

app = Flask(__name__)

#Route HomePage
@app.route('/')
def index():
    return "hello world !"

#Http://0.0.0.0:5000

if __name__ == "__main__":
    app.run(port = 5000)