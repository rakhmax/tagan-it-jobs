import requests
import json
from flask import jsonify, make_response, session
from .. import app
from .. import db

@app.route('/api/favorites', methods = ['GET', 'POST'])
def api_favorites_page():
    if not session.get('is_logged_in'):
        return make_response(jsonify({'msg': 'Not logged in'}), 403)

    try:
        select = f'SELECT DISTINCT vacancy_id from favorites WHERE user_id = {session.get("is_logged_in")}'

        db.cursor.execute(select)
        vacancies_id = db.cursor.fetchall()

        if not vacancies_id:
            return make_response(jsonify({'msg': 'No vacancies'}), 422)
    except:
        return make_response(jsonify({'msg': 'Not working'}), 500)

    try:
        vacancies = []

        for vacancy_id in vacancies_id:
            item = json.loads(requests.get(f'https://api.hh.ru/vacancies/{vacancy_id[0]}').text)
            vacancy = {
                'id': item['id'],
                'url': item['alternate_url'],
                'name': item['name'],
                'employer': {
                    'name': item['employer']['name'] if item['employer']['name'] else None,
                    'logo': item['employer']['logo_urls']['90'] if item['employer']['logo_urls'] else None
                },
                'salary': {
                    'currency': 'руб.' if item['salary']['currency'] == 'RUR' else 'USD',
                    'from': item['salary']['from'],
                    'to': item['salary']['to']
                } if item['salary'] else None,
                # 'responsibility': item['snippet']['responsibility'] if item['snippet'] else None,
            }
            
            vacancies.append(vacancy)
    
        vacancies_json = json.loads(json.dumps(vacancies))

        return make_response(jsonify(vacancies_json), 200)

    except Exception as e:
        return make_response(jsonify({'msg': e}), 500)

@app.route('/api/favorites/delete/<id>', methods = ['DELETE'])
def delete_favorite(id):
    if not session.get('is_logged_in'):
        return make_response(jsonify({'msg': 'Unauthorized'}), 401)

    try:
        select = f'DELETE FROM favorites WHERE user_id = {session.get("is_logged_in")} AND vacancy_id = {id}'

        db.cursor.execute(select)
        db.conn.commit()

        return make_response(jsonify({'msg': 'Removed'}), 200)
    except :
        return make_response(jsonify({'msg': 'Server error'}), 500)



     
