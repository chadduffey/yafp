from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'chad'}
	posts = [
        {
            'author': {'username': 'duff'},
            'body': 'Beautiful day in Seattle!'
        },
        {
            'author': {'username': 'jwess'},
            'body': 'The Nun! What a movie!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)

