from src.categories import find_categories


def test_find_categories(transactions_3):
    category_list = ["Открытие вклада",
                     "Перевод организации",
                     "Перевод с карты на счет"]
    assert find_categories(transactions_3, category_list) == {'Открытие вклада': 1,
                                                              'Перевод организации': 1}


def test_find_categories_empty_cat_list(transactions_3):
    category_list = []
    assert find_categories(transactions_3, []) == {}


def test_find_categories_empty_trans_list():
    category_list = ["Открытие вклада",
                     "Перевод организации",
                     "Перевод с карты на счет"]
    assert find_categories([], category_list) == {}
