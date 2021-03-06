from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cart")
def portfolio():
    return render_template("cart.html")


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
