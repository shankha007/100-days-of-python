from flask import Flask

app = Flask(__name__)


def make_bold(fn):
    text = fn()

    def wrapper():
        return f"<b>{text}</b>"

    return wrapper


def make_emphasis(fn):
    text = fn()

    def wrapper():
        return f"<em>{text}</em>"

    return wrapper

def make_underlined(fn):
    text = fn()

    def wrapper():
        return f"<u>{text}</u>"

    return wrapper

@app.route('/')
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img width='200' src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTZtNXFqYzZyYWp2MTZ0ODNqZXpib2lyN2FlaWlxZnBhOXp2OGk1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Puc4FZWExJc0E/giphy.gif'>")


@app.route('/bye')
@make_bold
@make_emphasis
@make_underlined
def hello_bye():
    return "Bye!"


# @app.route('/username/<path:name>')
# def greet(name):
#     return f"Hello there {name}"

# @app.route('/username/<name>/<int:number>')
# def greet(name, number):
#     return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)
