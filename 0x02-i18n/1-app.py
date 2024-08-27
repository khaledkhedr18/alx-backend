#!/usr/bin/env python3
'''Task 0's Module'''
from flask import Flask, request
from flask_babel import Babel


class Config:
    '''Simple Config Class'''
    LANGUAGES = ['en', 'fr']


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)
babel.default_locale = app.config['BABEL_DEFAULT_LOCALE']
babel.default_timezone = app.config['BABEL_DEFAULT_TIMEZONE']


def get_locale():
    """
    Retrieves the best matching locale from the request's Accept-Language header.

    Args:
        None

    Returns:
        str: The best matching locale.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
