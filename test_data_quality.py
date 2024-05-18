import pytest
from unittest.mock import patch, Mock
from app import app
import numpy as np


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@patch('joblib.load', autospec=True)
@patch('numpy.log1p', autospec=True)
def test_predict_complete_data(mock_log1p, mock_load, client):
    """
    Тестирование предсказания с полными данными.
    """
    # Мокируем загрузку моделей и скалера
    mock_model = Mock()
    mock_model.predict.return_value = [123.456]
    mock_scaler = Mock()
    mock_scaler.transform.return_value = [[1, 2, 3, 4, 5, 6]]

    mock_load.side_effect = [mock_model, mock_scaler]
    mock_log1p.side_effect = lambda x: x + 1

    response = client.post('/predict', data={
        'crim': '0.01',
        'rm': '1',
        'age': '30',
        'dis': '2',
        'lstat': '3',
        'nox': '4'
    })

    assert response.status_code == 200
    expected_text = 'Predicted Price: $123456.00'
    assert expected_text in response.data.decode('utf-8')


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


@patch('joblib.load', autospec=True)
def test_predict_data_ranges(mock_load, client):
    """
    Тестирование предсказания с данными за пределами допустимых диапазонов.
    """
    mock_model = Mock()
    mock_model.predict.return_value = [123.456]
    mock_scaler = Mock()
    mock_scaler.transform.return_value = [[1, 2, 3, 4, 5, 6]]

    mock_load.side_effect = [mock_model, mock_scaler]

    response = client.post('/predict', data={
        'crim': '-0.01',  # Не должно быть отрицательным
        'rm': '1',
        'age': '150',  # Нереалистичное значение
        'dis': '2',
        'lstat': '3',
        'nox': '4'
    })

    assert response.status_code == 200
    assert 'Predicted Price: $123456.00' in response.data.decode('utf-8')