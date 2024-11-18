import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'fdabffe7cc667a7728ed2ce65dce37ff'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '7966'

def test_status_code():
  response = requests.get(url=f'{URL}/trainers')
  assert response.status_code == 200

def test_my_trainer_name():
  response = requests.get(url=f'{URL}/trainers', params={'trainer_id' : TRAINER_ID})
  assert response.json()['data'][0]['trainer_name'] == 'Боба'

