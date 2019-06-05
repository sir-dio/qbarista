""" qBarista: tasty web-served seismic quizzes.

This file implements the database management functionality for the app.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

import random

from database.models import Question

import sqlite3


def initialize():
    """ Initialize the database if needed. """

    connection = sqlite3.connect('database/alex.db')

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
                            max_score INTEGER NOT NULL,
                            quiz TEXT NOT NULL
                            );""")


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


def add_result(student, score, max_score, quiz):
    """ Adds a result to the table."""

    connection = sqlite3.connect('database/alex.db')

    query = """INSERT INTO results (student, score, max_score, quiz)
               VALUES (:student, :score, :max_score, :quiz);"""

    values = {
        'student': student,
        'score': score,
        'max_score': max_score,
        'quiz': quiz
    }

    with connection:
        cursor = connection.cursor()
        cursor.execute(query, values)


def check_if_result_already_logged(student, quiz):
    """ Checks whether the result is already logged iin the database. """

    connection = sqlite3.connect('database/alex.db')

    query = 'SELECT * FROM results WHERE student=:student AND quiz=:quiz;'

    values = {
        'student': student,
        'quiz': quiz
    }

    with connection:
        c = connection.cursor()
        c.execute(query, values)

        results = c.fetchall()

    return True if results else False


def get_questions_by_quiz_id(quiz_id):
    """ Returns a list of questions for a given quiz id. """

    connection = sqlite3.connect('database/alex.db')

    with connection:
        cursor = connection.cursor()

        q = cursor.execute('SELECT * FROM questions WHERE quiz_id=?', [quiz_id])
        questions = q.fetchall()

    return [Question.create_from_db_entry(q) for q in questions]


def get_quiz_ids_by_quiz_name(quiz_name):
    """ Returns a list of existing quiz_ids for a given quiz name. """

    connection = sqlite3.connect('database/alex.db')

    with connection:
        cursor = connection.cursor()

        q = cursor.execute("SELECT DISTINCT quiz_id FROM questions")
        ids = q.fetchall()

    return [i[0] for i in ids if quiz_name in i[0]]


def get_question_by_id(question_id):
    """ Returns a question with the given ID. """

    connection = sqlite3.connect('database/alex.db')

    with connection:
        cursor = connection.cursor()

        q = cursor.execute("SELECT * FROM questions  WHERE id=?", [question_id])

    return Question.create_from_db_entry(q.fetchone())


def get_question_ids_by_quiz_id(quiz_id):
    """ Returns a list of question IDs for a given quiz ID. """

    connection = sqlite3.connect('database/alex.db')

    with connection:
        cursor = connection.cursor()

        q = cursor.execute('SELECT id FROM questions WHERE quiz_id=?', [quiz_id])

    return [i[0] for i in q.fetchall()]
