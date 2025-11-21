"""Example of flask main file."""
import os
from flask import Flask

app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return f'Response received from pod: {os.getenv("HOSTNAME")}'


if __name__ == '__main__':
    app.run()
