# Используйте официальный образ Python как базовый
FROM python:3.11

# Установите рабочую директорию в контейнере
WORKDIR /app

# Установите необходимые системные зависимости
RUN apt-get update && \
    apt-get install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*  # Очистка кэша APT для уменьшения размера образа

# Создайте виртуальное окружение
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Копируем файлы проекта в контейнер
COPY . .

# Установите Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска приложения при старте контейнера
CMD ["python3", "app.py"]

