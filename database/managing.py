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
        cursor.execute("""CREATE TABLE IF NOT EXISTS quizzes(
                            id TEXT PRIMARY KEY,
                            name TEXT NOT NULL,
                            var INTEGER NOT NULL
                            );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS questions(
                            id INTEGER PRIMARY KEY, 
                            question TEXT NOT NULL UNIQUE,
                            correct1 TEXT NOT NULL,
                            correct2 TEXT NOT NULL,
                            correct3 TEXT NOT NULL,
                            correct4 TEXT NOT NULL,
                            incorrect1 TEXT NOT NULL,
                            incorrect2 TEXT NOT NULL,
                            incorrect3 TEXT NOT NULL,
                            incorrect4 TEXT NOT NULL,
                            incorrect5 TEXT NOT NULL,
                            incorrect6 TEXT NOT NULL,
                            incorrect7 TEXT NOT NULL,
                            quiz_id TEXT NOT NULL,
                            FOREIGN KEY (quiz_id) REFERENCES quizzes(id)
                            );""")

        cursor.execute("""CREATE TABLE IF NOT EXISTS results(
                            id INTEGER PRIMARY KEY,
                            student TEXT NOT NULL,
                            score INTEGER NOT NULL,
                            quiz TEXT NOT NULL,
                            FOREIGN KEY (quiz) REFERENCES quizzes(name)
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
        c = connection.cursor()

        c.execute('DROP TABLE IF EXISTS answers;')
        c.execute('DROP TABLE IF EXISTS quizzes;')
        c.execute('DROP TABLE IF EXISTS results;')


if __name__ == '__main__':
    drop_all()
    initialize()
