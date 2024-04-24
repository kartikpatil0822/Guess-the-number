import random

from flask import Flask

app = Flask(__name__)


def guess_the_number(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        if int(result) > number:
            return ('<h3>Too High<h3>'
                    '<iframe src="https://giphy.com/embed/42BtVfS6BxcHgIT59m" width="480" height="270" frameBorder="0" '
                    'class="giphy-embed" allowFullScreen></iframe>')
        elif int(result) < number:
            return ('<h3>Too Low<h3>'
                    '<iframe src="https://giphy.com/embed/42BtVfS6BxcHgIT59m" width="480" height="270" frameBorder="0" '
                    'class="giphy-embed" allowFullScreen></iframe>')
        else:
            return (f'<h2>Your guess is correct {result}<h2>'
                    '<iframe src="https://giphy.com/embed/IS6CvSgqzzv4T1LMDj" width="480" height="270" frameBorder="0" '
                    'class="giphy-embed" allowFullScreen></iframe>')

    return wrapper


@app.route("/")
def index():
    return ('<h3>Guess the number<h3>'
            '<iframe src="https://giphy.com/embed/Rs2QPsshsFI9zeT4Kn" width="480" height="480" frameBorder="0" '
            'class="giphy-embed" allowFullScreen></iframe>')


@app.route("/<int:num>")
@guess_the_number
def guess(num):
    return f"{num}"


if __name__ == "__main__":
    number = random.randint(0, 9)
    app.run(debug=True)
