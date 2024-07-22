from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.exceptions import APIException
from rest_framework import status
def custom_exception_handler(exc, context):
    # Вызовите стандартный обработчик исключений DRF, чтобы получить стандартный ответ
    response = exception_handler(exc, context)

    # Если стандартный обработчик вернул ответ, то модифицируем его
    if response is not None:
        # Проверяем, что это не 500 ошибка
        if response.status_code != 500:
            # Создаем новый ответ с пользовательским сообщением
            response.data = exc.detail

    return response

class CustomAPIException(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, code):
        super().__init__(detail, code)
        self.status_code = code
        self.detail = detail