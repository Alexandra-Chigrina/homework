import os
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str | None] = None) -> Callable:
    """
    Декоратор автоматически логирует начало и конец выполнения функции, ее результаты и
    возникшие ошибки
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
            except Exception as e:
                result = None
                message = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"

            if filename:
                os.makedirs("logs", exist_ok=True)  # создаем директорию 'logs'
                path_to_filename = os.path.join("logs", filename)
                with open(path_to_filename, "a", encoding="utf-8") as file:
                    file.write(message + "\n")  # если filename задан, записываем сообщение в файл
            else:
                print(message)  # если filename не задан, выводим сообщение в консоль

            return result

        return wrapper

    return decorator
