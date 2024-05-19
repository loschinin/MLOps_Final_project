import pytest
from unittest.mock import patch, Mock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict_missing_data(client):
    """
    Тестирование предсказания с отсутствующими данными.
    """
    response = client.post('/predict', data={
        'crim': '0.01',
        'rm': '1',
        'age': '',
        'dis': '2',
        'lstat': '3',
        'nox': '4'
    })

    assert response.status_code == 200
    assert 'could not convert string to float' in response.data.decode('utf-8')

def test_predict_invalid_data(client):
    """
    Тестирование предсказания с некорректными данными.
    """
    response = client.post('/predict', data={
        'crim': 'invalid',
        'rm': '1',
        'age': '30',
        'dis': '2',
        'lstat': '3',
        'nox': '4'
    })

    assert response.status_code == 200
    assert 'could not convert string to float' in response.data.decode('utf-8')
