import requests
import json
from flask import jsonify, make_response, session
from .. import app
from .. import db

@app.route('/api/vacancies/<page>', methods = ['GET', 'POST'])
def api_vacancies_page(page):
    data = json.loads(requests.get(f'https://api.hh.ru/vacancies?area=1550&industry=7&page={page}&per_page=10').text)

    total_vacancies = data['found']
    total_pages = data['pages']

    vacancies_id = []

    if 'is_logged_in' in session:
        select = f'SELECT DISTINCT vacancy_id from favorites WHERE user_id = {session.get("is_logged_in")}'

        db.cursor.execute(select)
        vacancies_id = db.cursor.fetchall()

    try:
        vacancies = []
        
        for item in data['items']:
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
                'responsibility': item['snippet']['responsibility'],
            }
                
            vacancies.append(vacancy)

        final_json = {
            'vacancies': vacancies,
            'total_vacancies': total_vacancies,
            'total_pages': total_pages,
            'favorites': vacancies_id
        }
    
        vacancies_json = json.loads(json.dumps(final_json))

        return make_response(jsonify(vacancies_json), 200)

    except Exception as e:
        print(e)

@app.route('/api/vacancies/favorite/<id>', methods = ['GET', 'POST'])
def api_favorites(id):
    if not 'is_logged_in' in session:
        return make_response(jsonify({'msg': 'Not logged in'}), 401)

    insert_favorite_query = f'INSERT INTO favorites (user_id, vacancy_id) VALUES ({session.get("is_logged_in")}, {id})'

    try:
        db.cursor.execute(insert_favorite_query)
        db.conn.commit()

        return make_response(jsonify({'msg': 'Added'}), 200)

    except:
        return make_response(jsonify({'msg': 'Unable to add'}), 500)

