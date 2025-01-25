from src.string_search import search_string_in_description


def test_search_string_in_description(transactions_3):
    assert search_string_in_description(transactions_3, 'Открытие вклада') == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }
    ]


def test_search_string_not_find(transactions_3):
    assert search_string_in_description(transactions_3, 'Перевод с карты') == []


def test_search_string_empty_list():
    assert search_string_in_description([{}], 'Открытие счета') == []
