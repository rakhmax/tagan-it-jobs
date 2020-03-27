from flask import jsonify, request, session, abort, make_response
from .. import app
from .. import db
import hashlib

@app.route('/api/changepassword', methods = ['GET', 'POST'])
def api_change_password():
    if not 'user_id' in session:
        return make_response(jsonify(msg = 'Unauthorized'), 401)

    password = hashlib.sha256(request.form.get('password').encode()).hexdigest()
    passwordNew = hashlib.sha256(request.form.get('passwordNew').encode()).hexdigest()

    select_query = f'SELECT * FROM users WHERE id = {session.get("user_id")} AND password = "{password}"'

    db.cursor.execute(select_query)
    user = db.cursor.fetchone()

    if not user:
        return make_response(jsonify(msg = 'Неверный пароль'), 409)

    update_query = f'UPDATE users SET password = "{passwordNew}" WHERE id = "{session.get("user_id")}"'

    db.cursor.execute(update_query)

    return make_response(jsonify(msg = 'Пароль обновлен'), 200)
