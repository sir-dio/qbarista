""" qBarista: tasty web-served seismic quizzes.

This file the models to be used with the database.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""


class Test:
    """ A class representing a quiz. """

    def __init__(self, id=None, name=None, var=None):
        self.id = id
        self.name = name
        self.var = var

    def load_from_database(self):
        pass
