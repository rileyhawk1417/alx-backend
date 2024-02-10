#!/usr/bin/env python3
"""Run a simple index page"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Config for babel"""
    DEBUG = True
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def index() -> str:
    """Home Page
    Returns:
        html: html rendered page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
