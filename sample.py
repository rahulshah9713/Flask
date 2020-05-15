from flask import Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

mysql = MySQL(app)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Hello, World!"

@app.errorhandler(404)
def error(e):
    return "This page is not available"

if __name__ == "__main__":
    app.run(debug=True)