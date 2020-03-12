from flask import jsonify, request, session, abort, make_response
from .. import app

@app.route('/api/logout', methods = ['GET', 'POST'])
def api_logout():
    session.clear()

    return make_response(jsonify(msg = 'Logged out'), 200)
