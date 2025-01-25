import json
import logging
import os.path

logger = logging.getLogger("utils")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..", "logs", "utils.log"), "w", encoding="utf-8"
)
file_formatter = logging.Formatter("{asctime} {filename} {levelname}: {message}", style="{")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_financial_transactions(path: str) -> list[dict]:
    """
    Принимает на вход путь до JSON-файла, возвращает список словарей с данными
    о финансовых транзакциях
    """

    logger.info("Открываем файл")
    try:
        with open(path, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                logger.info("Файл открыт")
                return transactions
            else:
                logger.error("Неверный тип данных")
                return []
    except json.JSONDecodeError:
        logger.error("Невозможно преобразовать данные")
        return []
    except FileNotFoundError:
        logger.error(f"Файл {path} не найден")
        return []


path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")

# if __name__ == "__main__":
#     result = get_financial_transactions(path_to_file)
#     print(result)
