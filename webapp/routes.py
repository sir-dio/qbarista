""" qBarista: tasty web-served seismic quizzes.

This file defines the routes that are used for the web application.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from webapp import app
from flask import render_template, redirect, request, session, url_for
import database.managing as db

import random
from pprint import pprint


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ The login page. """

    if request.method == 'POST':
        if request.form['name'] != '':
            session['student'] = request.form['name']

    if 'student' not in session:
        return render_template('login.html')
    else:
        return redirect(url_for('quiz'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """ Serves the current quiz. """

    # check if the student si logged in
    if 'student' not in session:
        return redirect(url_for('login'))

    # initialize a new session if one is not already in progress
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0

        variants = db.get_quiz_ids_by_quiz_name(app.CURRENT_QUIZ)
        var = random.choice(variants)
        session['question_ids'] = db.get_question_ids_by_quiz_id(var)
        random.shuffle(session['question_ids'])

    # handle a post request
    if request.method == 'POST':
        # check question, update score

        # grab the question that was answered
        q = db.get_question_by_id(session['question_ids'][session['current_question']])
        # send the list of chosen answers to .check_answer() method and update the score
        session['score'] += q.check_answer(list(request.form.to_dict().keys()))

        session['current_question'] += 1

    # check if all the questions have been answered already
    if session['current_question'] >= len(session['question_ids']):
        return redirect('results')

    # grab the question to display next
    q = db.get_question_by_id(session['question_ids'][session['current_question']])

    return render_template('quiz.html',
                           title=app.CURRENT_QUIZ,
                           question=q)


@app.route('/results')
def results():
    """ Page with quiz results. """

    if 'student' not in session:
        return redirect(url_for('login'))

    if session['current_question'] < len(session['question_ids']):
        return redirect(url_for('quiz'))

    if not db.check_if_result_already_logged(session['student'], app.CURRENT_QUIZ):
        db.add_result(
            student=session['student'],
            score=session['score'],
            max_score=len(session['question_ids']),
            quiz=app.CURRENT_QUIZ
        )

    return render_template('result.html',
                           score=session['score'],
                           total=len(session['question_ids']))
