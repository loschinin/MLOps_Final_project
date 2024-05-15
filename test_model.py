import pytest
from unittest.mock import patch, Mock
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('joblib.load', autospec=True)
@patch('numpy.log1p', autospec=True)
def test_predict(mock_log1p, mock_load, client):
    """
    Тестирование маршрута предсказания.
    """
    # Мокируем загрузку моделей и скалера
    mock_model = Mock()
    mock_model.predict.return_value = [123456]
    mock_scaler = Mock()

    # Фиктивные имена признаков
    feature_names = ['crim', 'rm', 'age', 'dis', 'lstat', 'nox']

    # Мокируем transform для скалера, включая имена признаков
    mock_scaler.transform.return_value = [[1, 2, 3, 4, 5, 6]], feature_names

    mock_load.side_effect = [
        mock_model,
        mock_scaler
    ]

    # Мокируем log1p для numpy
    mock_log1p.return_value = 2

    # Отправляем POST-запрос на маршрут /predict
    response = client.post('/predict', data={
        'crim': '0.01',
        'rm': '1',
        'age': '30',
        'dis': '2',
        'lstat': '3',
        'nox': '4'
    })

    # Проверяем, что ответ имеет статус 200
    assert response.status_code == 200

    # Проверяем, что в ответе содержится ожидаемый текст
    expected_text = 'Predicted Price: $2383.66'
    assert expected_text in response.data.decode('utf-8')
