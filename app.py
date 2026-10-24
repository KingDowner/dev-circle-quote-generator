"""The Dev Circle starter Flask server."""
import random
from flask import Flask, jsonify, render_template

app = Flask(__name__)

QUOTES = [
    {"text": "Every great developer starts somewhere.", "author": "The Dev Circle"},
    {"text": "Small steps still move you forward.", "author": "The Dev Circle"},
    {"text": "The best way to learn is to build.", "author": "The Dev Circle"},
    {"text": "A bug is a clue, not a dead end.", "author": "The Dev Circle"},
    {"text": "Progress beats perfection.", "author": "The Dev Circle"},
]

@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/quote")
def get_quote():
    # TODO (Python teammate): pick randomly from a list of quotes.
    return jsonify(random.choice(QUOTES))


if __name__ == "__main__":
    # Development only: do not deploy with debug enabled.
    app.run(debug=True)
