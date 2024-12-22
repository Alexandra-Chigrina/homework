from typing import Generator, Iterator


def filter_by_currency(transactions: list[dict], currency_type: str) -> Iterator[dict]:
    """
    Принимает на вход список словарей с транзакциями, возвращает итератор,
    выдающий транзакции с заданной валютой операции
    """
    if not transactions:
        return iter([])
    if currency_type not in ["USD", "RUB"]:
        return iter([])

    filtered_by_curr_trans = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency_type, transactions)
    return filtered_by_curr_trans


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    Принимает список словарей, возвращает описание каждой операции по очереди
    """
    if not transactions:
        return
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int) -> Generator:
    """
    Генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до
    9999 9999 9999 9999
    """
    if start > end:
        raise ValueError("Ошибка вводных данных")
    if start < 0 or end < 0:
        raise ValueError("Вводные данные не могут быть отрицательными")
    for i in range(start, end + 1):
        number = "0" * (16 - len(str(i))) + str(i)
        yield f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
