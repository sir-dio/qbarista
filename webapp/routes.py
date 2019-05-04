from webapp import app


@app.route('/')
def home():
    return '<h1>Welcome home</h2>'
