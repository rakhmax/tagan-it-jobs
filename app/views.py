from flask import Flask, render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html', name="Max")

@app.route('/test')
def test():
    return render_template('test.html')
