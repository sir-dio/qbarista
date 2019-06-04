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

    def check_answer(self, answer):
        """ Checks the answer and returns the score. """

        answer.sort()
        correct = [a for a in self.correct if a]
        correct.sort()

        return 1 if answer == correct else 0

    @property
    def answers(self):
        """ Returns a shuffled list of answers. """

        answers = [answer for answer in self.correct + self.incorrect if answer]
        random.shuffle(answers)
        return answers

    def __str__(self):
        string = '[%s] %s\n\t* ' % (self.quiz_id, self.question)
        string += '\n\t* '.join(self.answers)
        return string

    def __repr__(self):
        return '[%s]: %s\n' % (self.quiz_id, self.question)

    @classmethod
    def create_from_db_entry(cls, entry):
        """ Creates a Question instance from a database entry. """

        out = Question()

        out.ID = entry[0]

        out.question = entry[1]
        out.correct = [entry[i] for i in range(2, 6)]
        out.incorrect = [entry[i] for i in range(6, 13)]
        out.picture = entry[13]
        out.quiz_id = entry[14]

        return out
