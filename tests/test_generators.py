from unittest import expectedFailure

import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_1):
    filtered_transactions = filter_by_currency(transactions_1, "RUB")
    assert next(filtered_transactions) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    assert next(filtered_transactions) == {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    with pytest.raises(StopIteration):
        assert next(filtered_transactions)


def test_filter_by_currency_other_currency(transactions_1):
    filtered_transactions = filter_by_currency(transactions_1, "EUR")
    assert not list(filtered_transactions)


def test_filter_by_currency_empty():
    filtered_transactions = filter_by_currency([], "USD")
    assert not list(filtered_transactions)


def test_filter_by_currency_no_currency(transactions_2):
    filtered_transactions = filter_by_currency(transactions_2, "USD")
    assert not list(filtered_transactions)


def test_transaction_descriptions(transactions_1):
    generator = transaction_descriptions(transactions_1)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"
    with pytest.raises(StopIteration):
        assert next(generator)


def test_transaction_descriptions_empty():
    generator = transaction_descriptions([])
    assert not list(generator)


def test_filter_by_currency_no_currency(transactions_2):
    filtered_transactions = filter_by_currency(transactions_2, "USD")
    assert not list(filtered_transactions)


@pytest.mark.parametrize("start, end, expected", [
    (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
    (8425652565842563, 8425652565842565, ["8425 6525 6584 2563", "8425 6525 6584 2564", "8425 6525 6584 2565"]),
    (9999999999999997, 9999999999999999, ["9999 9999 9999 9997", "9999 9999 9999 9998", "9999 9999 9999 9999"])])
def test_card_number_generator(start, end, expected):
    generator = list(card_number_generator(start, end))
    assert generator == expected


def test_card_number_generator_error():
    with pytest.raises(ValueError) as error:
        list(card_number_generator(5,2))
    assert str(error.value) == "Ошибка вводных данных"


def test_card_number_generator_negative_arg():
    with pytest.raises(ValueError) as error:
        list(card_number_generator(-7,5))
    assert str(error.value) == "Вводные данные не могут быть отрицательными"
