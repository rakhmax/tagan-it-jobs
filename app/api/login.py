from flask import jsonify, request, session, abort, make_response
from .. import app
from .. import db
import hashlib

@app.route('/api/signin', methods = ['GET', 'POST'])
def api_signin():
    email = request.form.get('email')
    password = hashlib.sha256(request.form.get('password').encode()).hexdigest()

    select_query = f'SELECT * FROM users WHERE email = "{email}" AND password = "{password}"'

    db.cursor.execute(select_query)
    user = db.cursor.fetchone()

    if not user:
        return make_response(jsonify({'msg': 'User does not exist'}), 422)

    session['is_logged_in'] = user[0]

    return make_response(jsonify({'msg': 'Logged in'}), 200)
