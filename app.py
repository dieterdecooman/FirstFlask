## A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',active='home')

@app.route('/link')
def link():
    return render_template('index.html',active='link')

if __name__ == '__main__':
    app.run()
