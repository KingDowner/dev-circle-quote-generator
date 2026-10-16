"""The Dev Circle starter Flask server."""
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/api/quote")
def get_quote():
    # TODO (Python teammate): pick randomly from a list of quotes.
    return jsonify({"text": "Every great developer starts somewhere.", "author": "The Dev Circle"})


if __name__ == "__main__":
    # Development only: do not deploy with debug enabled.
    app.run(debug=True)
