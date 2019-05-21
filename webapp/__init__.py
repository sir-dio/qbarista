""" qBarista: tasty web-served seismic quizzes.

This file initializes the web application.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from flask import Flask

app = Flask(__name__)

from webapp import routes
