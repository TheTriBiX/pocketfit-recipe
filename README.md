Перед стартом перейти в директорию pocketfit-recipe/pocketfit

docker-compose up --build


чтобы сменить sqlite на postgres:

в файле settings.py

Убрать комментарии:

 DATABASES = {
     "default": {
         "ENGINE": "django.db.backends.postgresql",
         "NAME": env("DB_NAME"),
         "USER": env("DB_USER"),
         "PASSWORD": env("DB_PASSWORD"),
         "HOST": env("DB_HOST"),
         "PORT": env("DB_PORT"),
     }
 }

Добавить комментарии
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

создать файл .env(рядом с manage.py) 
