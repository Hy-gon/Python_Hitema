import sys, os
from flask import Flask, render_template

app = Flask(__name__)

#Route HomePage
@app.route('/')
def index():
    return render_template('index.html')

#Http://0.0.0.0:5000

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = os.environ.get("PORT", 5000), debug=True)