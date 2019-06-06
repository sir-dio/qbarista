from webapp import app

app.ALEX = {
    'current_quiz': 'TOMO',
    'logged_in_students': '',
    'admin_register_url': '/keep_calm_and_quiz',
    'admin_present': False,
}

app.run(debug=True)
