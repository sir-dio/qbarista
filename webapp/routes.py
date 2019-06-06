""" qBarista: tasty web-served seismic quizzes.

This file defines the routes that are used for the web application.

@author: sir-dio
e-mail: dubrovin.io@icloud.com

"""

from webapp import app
from flask import render_template, redirect, request, session, url_for
import database.managing as db

import random


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ The login page. """

    # log the student in
    if request.method == 'POST':
        if request.form['name'] != '':
            name = request.form['name']
            session['student'] = name

            # log the student to track progress
            app.ALEX['logged_in_students'].append(name)

    # handle GET requests
    if 'student' not in session:
        return render_template('login.html', title=app.ALEX['current_quiz'])
    else:
        return redirect(url_for('quiz'))


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """ Serves the current quiz. """

    # check if the student is logged in
    if 'student' not in session:
        return redirect(url_for('login'))

    # initialize a new session if one is not already in progress
    if 'current_question' not in session:
        session['current_question'] = 0
        session['score'] = 0
        session['correct_answer_shown'] = False
        session['random_seed'] = random.randint(1, 1024)

        variants = db.get_quiz_ids_by_quiz_name(app.ALEX['current_quiz'])
        var = random.choice(variants)
        session['question_ids'] = db.get_question_ids_by_quiz_id(var)
        random.shuffle(session['question_ids'])

    # handle a post request
    if request.method == 'POST':
        # grab the question that was answered
        q = db.get_question_by_id(session['question_ids'][session['current_question']])

        # send the list of chosen answers to .check_answer() method and update the score
        chosen_answers = list(request.form.to_dict().keys())
        score = q.check_answer(chosen_answers)
        session['score'] += score

        # update the current question index
        session['current_question'] += 1

        # return the page with the correct answer
        return render_template('quiz.html',
                               title=app.ALEX['current_quiz'],
                               question=q,
                               random_seed=session['random_seed'],
                               show_correct_answer=True,
                               chosen_answers=chosen_answers,
                               score=score,
                               total_questions=len(session['question_ids']),
                               current_question=session['current_question'])

    # check if all the questions have been answered already
    if session['current_question'] >= len(session['question_ids']):
        return redirect('results')

    # grab the question to display next
    q = db.get_question_by_id(session['question_ids'][session['current_question']])

    return render_template('quiz.html',
                           title=app.ALEX['current_quiz'],
                           question=q,
                           random_seed=session['random_seed'],
                           show_correct_answer=False,
                           total_questions=len(session['question_ids']),
                           current_question=session['current_question'] + 1)


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
                           title=app.ALEX['current_quiz'],
                           score=session['score'],
                           total=len(session['question_ids']))


@app.route(app.ALEX['admin_register_url'])
def register_admin():
    """ A one-time link to create an admin session. """

    if not app.ALEX['admin_present']:
        session['is_admin'] = True

    return redirect(url_for('admin'))


@app.route('/admin')
def admin():
    """ Page for the teacher to keep track of students. """

    if not session.get('is_admin'):
        return redirect(url_for('login'))

    return render_template('admin.html',
                           title='Admin Page (%s)' % app.ALEX['current_quiz'],

                           )
