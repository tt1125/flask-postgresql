from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="front/out", static_url_path="")


@app.route("/")
def index():
    return send_from_directory("front/out", "index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)