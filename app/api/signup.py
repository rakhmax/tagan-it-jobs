from flask import jsonify, request, abort, make_response
from .. import app
from .. import db
import hashlib

@app.route('/api/signup', methods=['POST'])
def api_signup():
    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    email = request.form.get('email')
    password = hashlib.sha256(request.form.get('password').encode()).hexdigest()
    agreement = request.form.get('agreement')

    if not agreement:
        return make_response(jsonify({'msg': 'You need to apply the agreement'}), 409)

    create_query = f'INSERT INTO users (firstname, lastname, email, password) VALUES ("{firstname}", "{lastname}", "{email}", "{password}")'
    select_query = f'SELECT firstname, lastname, email FROM users WHERE email = "{email}"'

    try:
        db.cursor.execute(select_query)
        user = db.cursor.fetchone()

        if user:
            return make_response(jsonify({'msg': 'User already exists'}), 422)

    except:
        return make_response(jsonify({'msg': 'Unable to create user'}), 500)

    try:
        db.cursor.execute(create_query)
        db.conn.commit()

        return jsonify({'msg': 'Thank you for registration'})
    except:
        return make_response(jsonify({'msg': 'Unable to create user'}), 500)

    

    