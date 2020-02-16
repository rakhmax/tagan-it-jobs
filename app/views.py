from flask import render_template, session, redirect
from . import app
from . import db

def get_user():
    select_query = f'SELECT firstname, lastname FROM users WHERE id={session.get("is_logged_in")}'

    db.cursor.execute(select_query)
    user = db.cursor.fetchone()
    return f'{user[0]} {user[1]}'

@app.route('/')
def home():
    user = None
    
    if session.get('is_logged_in'):
        user = get_user()

    return render_template('index.html', name = user)

@app.route('/signup')
def signup():
    return render_template('signup.html', title = 'Sign up')

@app.route('/signin')
def signin():
    if session.get('is_logged_in'):
        return redirect('/dashboard')

    return render_template('signin.html', title = 'Sign in')

@app.route('/dashboard')
def dashboard():
    if not session.get('is_logged_in'):
        return redirect('/signin')

    user = get_user()

    return render_template('dashboard.html', title = 'Dashboard', name = user)
