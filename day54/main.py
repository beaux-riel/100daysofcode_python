from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/bye")
def goodbye_world():
    return "<h1>Goodbye, World!</h1>"

@app.route("/username/<name>")
def greet(name):
    return f'Hello {name}!'

if __name__ == "__main__":
    app.run()