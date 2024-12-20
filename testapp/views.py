from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def test_error(request):
    try:
        raise ValueError("Это тестовая ошибка для проверки логирования.")
    except ValueError as e:
        logger.error("Произошла ошибка: %s", e, exc_info=True)
        return HttpResponse("Ошибка вызвана и логирована.")
