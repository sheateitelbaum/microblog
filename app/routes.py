from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Shea'}
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'HELLO'
        },
        {
            'author':{'username': 'Susan'},
            'body': 'Goodbye'
        }
    ]
    return render_template('index.html',  user=user,posts=posts)