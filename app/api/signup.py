from flask import jsonify, request
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

    create_query = f'INSERT INTO Users (Firstname, Lastname, Email, Password) VALUES ("{firstname}", "{lastname}", "{email}", "{password}")'
    select_query = f'SELECT Firstname, Lastname, Email FROM Users WHERE Email = "{email}"'

    db.cursor.execute(select_query)
    user = db.cursor.fetchone()

    if not agreement:
        return jsonify({'msg': 'User did not apply the agreement', 'code': 1001}), 501

    if user:
        return jsonify({'msg': 'User already exists', 'code': 1002}), 501

    try:
        db.cursor.execute(create_query)
        db.conn.commit()

        return jsonify({'msg': 'Thank you for registration', 'code': 1000})
    except:
        return 'Unable to create user', 501

    

    