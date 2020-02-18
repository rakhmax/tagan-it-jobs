from flask import render_template, session, redirect, request, Request, jsonify
import requests
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
    if session.get('is_logged_in'):
        return redirect('/favorites')
        
    return render_template('signup.html', title = 'Регистрация')


@app.route('/login')
def login():
    if session.get('is_logged_in'):
        return redirect('/favorites')

    return render_template('login.html', title = 'Вход')


@app.route('/vacancies')
def vacancies():
    user = None

    if session.get('is_logged_in'):
        user = get_user()

    return render_template('vacancies.html', title = 'Все вакансии', name = user)


@app.route('/favorites')
def favorites():
    if not session.get('is_logged_in'):
        return redirect('/login')

    user = get_user()

    return render_template('favorites.html', title = 'Избранное', name = user)


@app.route('/settings')
def settings():
    if not session.get('is_logged_in'):
        return redirect('/login')

    user = get_user()

    return render_template('settings.html', title = 'Настройки', name = user)
