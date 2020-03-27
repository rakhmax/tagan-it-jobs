from flask import jsonify, session, make_response
from .. import app

@app.route('/api/logout', methods = ['GET', 'POST'])
def api_logout():
    session.clear()

    return make_response(jsonify(msg = 'Выполнен выход'), 200)
