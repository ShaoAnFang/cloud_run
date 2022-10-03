import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route('/GGWP', methods=['GET'])
def test():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
