import requests
import json
from flask import jsonify, make_response
from .. import app
from .. import db

@app.route('/api/vacancies/<page>', methods = ['GET', 'POST'])
def api_vacancies_page(page):
    data = json.loads(requests.get(f'https://api.hh.ru/vacancies?area=1550&industry=7&page={page}').text)

    total_vacancies = data['found']
    total_pages = data['pages']

    try:
        vacancies = []

        for item in data['items']:
            vacancy = {
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
            'total_pages': total_pages
        }
    
        vacancies_json = json.loads(json.dumps(final_json))

        return make_response(jsonify(vacancies_json), 200)

    except Exception as e:
        print(e)

