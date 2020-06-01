from datetime import datetime
from flask import Flask, render_template, request
from os import environ


def create_application():
    app = Flask(__name__)
    app.secret_key = environ['FLASK_SECRET_KEY']

    return app


application = create_application()


@application.route('/', methods=['GET'])
def home():
    return render_template(
        'index.html',
        year=datetime.now().year,
    )


@application.route('/board', methods=['GET'])
def board():
    from .boggle.src.boggle import boggle_web

    seed = request.args.get('seed')
    b = boggle_web(seed)
    split_board = [b[:4], b[4:8], b[8:12], b[12:]]

    return render_template(
        'board.html',
        year=datetime.now().year,
        board=split_board,
        seed=seed
    )


if __name__ == '__main__':
    application.debug = True
    application.run()
