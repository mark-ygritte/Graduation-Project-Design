# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/__health')
def health_check():
    return 'OK'

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port="8000")