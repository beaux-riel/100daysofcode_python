from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph.</p>" \
            "<img src='https://i.chzbgr.com/full/7889288192/h1AD275FE/husky-puppies-on-the-porch-in-this-gif' width=200>"

@app.route("/bye")
# @make_bold
# @make_emphasis
# @make_underlined
def goodbye_world():
    return "<h1>Goodbye, World!</h1>"

@app.route("/username/<path:name>/<int:number>")
def greet(name, number):
    return f"Yo! What's going on {name}? Are you still {number} years old?"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)