Перед стартом

/manage.py makemigrations

/manage.py migrate

sudo docker build . -t pocket-fit-recipes

sudo docker compose up -d

чтобы сменить sqlite на postgres:

в файле settings.py

Убрать комментарии:

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": env("DB_NAME"),
#         "USER": env("DB_USER"),
#         "PASSWORD": env("DB_PASSWORD"),
#         "HOST": env("DB_HOST"),
#         "PORT": env("DB_PORT"),
#     }
# }

Добавить комментарии
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

создать файл .env(рядом с manage.py) 