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


class Question:
    """ A class representing a question for the quiz. """

    def __init__(self, interactive=True):
        self.id = None
        self.question = None
        self.correct = []
        self.incorrect = []
        self.quiz_id = None

        if interactive:
            self.fill_interactively()

    def fill_interactively(self):
        """ Create a question interactively. """

        self.question = input('Вопрос: ')

        self.correct.append(input('Правильный ответ: '))
        for i in range(1, 4):
            additional = input('%sй дополнительный правильный ответ: ' % i)
            if not additional:
                break
            self.correct.append(additional)

        self.incorrect.append(input('1й неправильный ответ: '))
        for i in range(2, 8):
            additional = input('%sй неправильный ответ: ' % i)
            if not additional:
                break
            self.incorrect.append(additional)

        self.quiz_id = input('ID теста, к которому относится вопрос: ')
