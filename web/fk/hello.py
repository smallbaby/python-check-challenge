from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "index"


@app.route('/hello/<name>')
def hello(name):
    return 'Hello World' + name


@app.route("/limit/<int:num>")
def limit(num):
    return "limit" + str(num)


if __name__ == '__main__':
    app.run()
