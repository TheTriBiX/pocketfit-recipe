from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Вызовите стандартный обработчик исключений DRF, чтобы получить стандартный ответ
    response = exception_handler(exc, context)

    # Если стандартный обработчик вернул ответ, то модифицируем его
    if response is not None:
        # Проверяем, что это не 500 ошибка
        if response.status_code != 500:
            # Создаем новый ответ с пользовательским сообщением
            custom_response = {
                "message": str(exc)
            }
            response.data = custom_response

    return response