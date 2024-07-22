from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException

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

class CustomAPIException(APIException):
    status_code = 400
    default_detail = 'A custom error occurred.'
    default_code = 'custom_error'

    def __init__(self, detail=None, code=None):
        if detail is not None:
            self.detail = detail
        if code is not None:
            self.status_code = code