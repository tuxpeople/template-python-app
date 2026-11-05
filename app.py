"""Minimal Flask app. Replace with your application.

Served by gunicorn in the container (see Dockerfile); never enable Flask's
debug mode, the Werkzeug debugger allows code execution from the browser.
"""

import os

from flask import Flask, render_template

app = Flask(__name__)
APP_TITLE = os.environ.get("APP_TITLE", "Hello")


@app.route("/")
def index():
    return render_template("index.html", title=APP_TITLE)


@app.route("/healthz")
def healthz():
    return {"status": "ok"}


# Local development only, the container runs gunicorn
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
