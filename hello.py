import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! Kenneth is awesome. Robert is not. Joon is okay.'