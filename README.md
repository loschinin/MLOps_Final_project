MLOps_Final_project
MLOps. Final Project (vo_PJ) 2 semester

Над проектом работали

Чурсин Александр 
Лощинин Дмитрий 
Байгозин Павел 
кконен Алексей

Это Flask-приложение предсказывает цену на основе входных данных, используя предварительно обученную модель градиентного бустинга и стандартный скейлер.

Установка
Для запуска этого приложения вам понадобится Docker. Если Docker у вас еще не установлен, следуйте инструкциям на официальном сайте Docker.

Шаги установки
Склонируйте этот репозиторий:

git clone https://github.com/ваш_пользователь/flask-prediction-app.git
cd flask-prediction-app
Убедитесь, что у вас есть следующие файлы в корне проекта:

app.py - основной файл приложения Flask.
requirements.txt - файл с зависимостями.
selected_gradient_boosting_regressor.pkl - модель для предсказаний.
selected_standard_scaler.pkl - скейлер для предобработки данных.
templates/index.html - HTML-шаблон для формы ввода.
Соберите Docker образ:

docker build -t flask-prediction-app .
Запустите Docker контейнер:

docker run -p 5000:5000 flask-prediction-app
Приложение будет доступно по адресу http://localhost:5000.

Создание окружения
Вы также можете запустить проект локально, создав виртуальное окружение.

Создайте виртуальное окружение:

python3 -m venv myenv
Активируйте окружение (MacOS/Linux):

source myenv/bin/activate
Установите зависимости:

pip install --upgrade pip
pip install -r requirements.txt
Запустите проект:

python3 app.py
Использование
Перейдите на главную страницу приложения.

Введите необходимые данные в форму:

crim: уровень преступности
rm: количество комнат
age: возраст
dis: расстояние до центров занятости
lstat: процент низкостатусного населения
nox: уровень оксидов азота
Нажмите кнопку "Predict" для получения предсказания цены.

Тестирование
Для тестирования приложения используются pytest. Тесты находятся в файле test_data_quality.py.

Запуск тестов
Установите зависимости для тестирования:

pip install -r requirements.txt
Запустите тесты с помощью команды:

pytest test_data_quality.py
Структура проекта
app.py: Основной файл приложения Flask.
requirements.txt: Зависимости Python для проекта.
Dockerfile: Скрипт для сборки Docker образа.
templates/: Директория с HTML шаблонами.
index.html: Шаблон для формы ввода данных.
selected_gradient_boosting_regressor.pkl: Предобученная модель градиентного бустинга.
selected_standard_scaler.pkl: Стандартный скейлер для предобработки данных.
test_data_quality.py: Тесты для проверки качества данных и функциональности маршрута предсказания.
