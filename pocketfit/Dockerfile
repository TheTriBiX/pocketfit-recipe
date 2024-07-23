# Используем официальный образ Python в качестве базового образа
FROM python:3.11-slim

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Создаем директорию для приложения
RUN mkdir /code
WORKDIR /code

# Устанавливаем зависимости Python
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем проект в контейнер
COPY . /code/

# Выполняем миграции и собираем статические файлы
RUN python manage.py makemigrations recipeservice
RUN python manage.py migrate
# Открываем порт для веб-сервера
EXPOSE 8000

# Запускаем Django сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]