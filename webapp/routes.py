""" qBarista: tasty web-served seismic tests.

This file defines the roots that are used for the web application.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from webapp import app


@app.route('/')
def home():
    return '<h1>Welcome home</h2>'
