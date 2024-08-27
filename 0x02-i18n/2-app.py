#!/usr/bin/env python3
'''Task 0's Module'''
from flask import Flask, request, render_template
from flask_babel import Babel  # type: ignore


class Config:
    '''Simple Config Class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def get_index() -> str:
    """
    Defines a route for the root URL ('/') of the web application.

    Returns:
        The rendered HTML template located at '1-index.html'.
    """
    return render_template('1-index.html')


@babel.localeselector
def get_locale():
    """
    Selects the locale for the current request based on the Accept-Language header.

    Returns:
        The best matching locale from the list of available languages.
    """
    return request.accept_languages.best_match(['LANGUAGES'])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
