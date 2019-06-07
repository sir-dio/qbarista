from webapp import app

app.ALEX = {
    'current_quiz': 'MASW',
    'logged_in_students': [],
    'finished_students': [],
    'completion_percents': {},
    'scores': {},
    'admin_present': False,
}

app.run(debug=True, host='0.0.0.0')
