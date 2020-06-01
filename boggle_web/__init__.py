from datetime import datetime
from exceptions import EnvironmentUnsetError
from flask import Flask, render_template
from os import environ


def create_application():
    app = Flask(__name__)
    try:
        app.secret_key = environ['WFB_FLASK_SECRET_KEY']
    except KeyError:
        raise EnvironmentUnsetError('WFB_FLASK_SECRET_KEY')

    return app


application = create_application()


@application.route('/', methods=['POST', 'GET'])
def about():
    return render_template(
        'index.html',
        title=environ['WFB_PROJECT_NAME'],
        year=datetime.now().year,
    )


if __name__ == '__main__':
    application.debug = True
    application.run()
