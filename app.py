from flask import Flask, request, render_template
import joblib
import numpy as np

# Создание экземпляра приложения Flask
app = Flask(__name__)

# Загрузка модели и StandardScaler с использованием joblib
model = joblib.load('./selected_gradient_boosting_regressor.pkl')
scaler = joblib.load('./selected_standard_scaler.pkl')

# Маршрут для главной страницы, возвращает HTML-форму для ввода данных
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для обработки данных формы и выполнения предсказания
@app.route('/predict', methods=['POST'])
def predict():
    # Получение данных из формы
    try:
        crim = np.log1p(float(request.form['crim']))
        rm = float(request.form['rm'])
        age = float(request.form['age'])
        dis = float(request.form['dis'])
        lstat = float(request.form['lstat'])
        nox = float(request.form['nox'])

        # Создание массива для предсказания
        features = np.array([[crim, rm, age, dis, lstat, nox]])
        features_scaled = scaler.transform(features)

        # Предсказание
        prediction = model.predict(features_scaled)
        result = f'Predicted Price: ${prediction[0] * 1000:.2f}'
    except Exception as e:
        result = str(e)

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)