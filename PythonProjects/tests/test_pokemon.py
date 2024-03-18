import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'

HEADERS = {
    'Content-Type' : 'application/json',
    'trainer_token' : 'cb317ff3925c55ea0095a8771681cabb'
    }

TOKEN = 'cb317ff3925c55ea0095a8771681cabb'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 1832})
    assert response.status_code == 200
    

def test_part_of_response():
        response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : 1832})
        assert response.json()['data'][0]['trainer_name'] == 'Бот'