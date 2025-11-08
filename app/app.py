from flask import Flask
import os

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "v1")

@app.route("/")
def index():
    return f"Hello from web app — Version: {VERSION}\n"

@app.route("/healthz")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
