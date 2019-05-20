""" qBarista: tasty web-served seismic quizzes.

This file implements the database management functionality for the app.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import sqlite3


def initialize():
    """ Initialize the database if needed. """

    connection = sqlite3.connect('alex.db')

    with connection:
        cursor = connection.cursor()

        # create missing tables
        cursor.execute("""CREATE TABLE IF NOT EXISTS questions(
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            question TEXT NOT NULL,                            
                            correct1 TEXT NOT NULL,
                            correct2 TEXT,
                            correct3 TEXT,
                            correct4 TEXT,
                            incorrect1 TEXT NOT NULL,
                            incorrect2 TEXT,
                            incorrect3 TEXT,
                            incorrect4 TEXT,
                            incorrect5 TEXT,
                            incorrect6 TEXT,
                            incorrect7 TEXT,
                            picture TEXT,
                            quiz_id TEXT NOT NULL
                            );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS results(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            quiz_id TEXT NOT NULL,
                            FOREIGN KEY (quiz_id) REFERENCES quizzes(quiz_id)
                            );""")


def drop_all(force=False):
    """ Drops all the tables in the database.

    Parameters
    ----------
    force : bool
        A flag that disables verbal conformation.

    """

    if not force:
        if input('All tables will be dropped! Proceed? (y/[n])') != 'y':
            print('Aborting.')
            return

    connection = sqlite3.connect('alex.db')

    with connection:
        cursor = connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS questions;')
        cursor.execute('DROP TABLE IF EXISTS results;')


def add_question(question):
    """ Adds a question to the database. """

    connection = sqlite3.connect('database/alex.db')

    query = """INSERT INTO questions (question, correct1, correct2, correct3, correct4,
                       incorrect1, incorrect2, incorrect3, incorrect4,
                       incorrect5, incorrect6, incorrect7, picture, quiz_id)
                VALUES (:q, :c1, :c2, :c3, :c4, :i1, :i2, :i3, :i4, :i5, :i6, :i7,
                        :pic, :id); """

    values = {
        'q': question.question,
        'pic': question.picture,
        'id': question.quiz_id
    }

    for i, ans in enumerate(question.correct, 1):
        values['c%i' % i] = ans

    for i, ans in enumerate(question.incorrect, 1):
        values['i%i' % i] = ans

    with connection:
        cursor = connection.cursor()
        cursor.execute(query, values)
