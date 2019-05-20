""" qBarista: tasty web-served seismic quizzes.

This file the models to be used with the database.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import random


class Question:
    """ A class representing a question for the quiz. """

    def __init__(self, interactive=False):
        self.question = None
        self.correct = []
        self.incorrect = []
        self.picture = None
        self.quiz_id = None

        if interactive:
            self.fill_interactively()

    def fill_interactively(self):
        """ Create a question interactively. """

        # the question itself
        self.question = input('Вопрос: ')

        # first correct answer
        self.correct.append(input('Правильный ответ: '))

        # up to 3 additional correct answers
        for i in range(1, 4):
            additional = input('%sй дополнительный правильный ответ: ' % i)

            # if empty, fill the rest with None
            if not additional:
                for j in range(i, 4):
                    self.correct.append(None)
                break

            self.correct.append(additional)

        # first incorrect answer
        self.incorrect.append(input('1й неправильный ответ: '))

        # up to 6 additional incorrect answers:
        for i in range(2, 8):
            additional = input('%sй неправильный ответ: ' % i)

            # again, if empty, fill the rest with None
            if not additional:
                for j in range(i, 8):
                    self.incorrect.append(None)
                break

            self.incorrect.append(additional)

        # ID of the quiz
        self.quiz_id = input('ID теста, к которому относится вопрос: ')

    def add_picture(self, picture):
        """ Adds a picture to the question. """
        self.picture = picture

    @property
    def answers(self):
        return [answer for answer in self.correct + self.incorrect if answer]

    def __str__(self):
        repr = '%s\n' % self.question
        for answer in random.sample(self.answers, len(self.answers)):
            repr += '\t* %s\n' % answer
        return repr

    def __repr__(self):
        return '%s\n' % self.question
