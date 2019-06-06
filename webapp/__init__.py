""" qBarista: tasty web-served seismic quizzes.

This file initializes the web application.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import os

from flask import Flask

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.ALEX = {
    'admin_register_url': '/i_am_admin'
}

from webapp import routes
