from flask import jsonify, request, session, abort, make_response
from .. import app
from .. import db
import hashlib

@app.route('/api/login', methods = ['GET', 'POST'])
def api_login():
    email = request.form.get('email')
    password = hashlib.sha256(request.form.get('password').encode()).hexdigest()

    select_user_query = f'SELECT * FROM users WHERE email = "{email}"'

    db.cursor.execute(select_user_query)
    user = db.cursor.fetchone()

    if not user:
        return make_response(jsonify({'msg': 'User does not exist'}), 422)

    select_query = f'SELECT * FROM users WHERE email = "{email}" AND password = "{password}"'

    db.cursor.execute(select_query)
    user_password = db.cursor.fetchone()

    if not user_password:
        return make_response(jsonify({'msg': 'Password is incorrect'}), 409)

    session['is_logged_in'] = user[0]

    return make_response(jsonify({'msg': 'Logged in'}), 200)
