""" qBarista: tasty web-served seismic tests.

This file defines the roots that are used for the web application.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from webapp import app

from flask import render_template


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Welcome to Alex!')


@app.route('/test')
def test():
    return render_template('test.html')
