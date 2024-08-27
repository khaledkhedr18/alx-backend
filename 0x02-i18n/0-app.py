#!/usr/bin/env python3
'''Task 0's Module'''
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def get_index() -> str:
    """
    Defines a route for the root URL ('/') of the web application.

    Returns:
        The rendered HTML template located at '0-index.html'.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
