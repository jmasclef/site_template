import flask
import sys
from flask import Flask
from flask import render_template

sys.path.append(".")
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',name='World')

if __name__=='__main__':
    app.run(host="0.0.0.0", debug=True)

