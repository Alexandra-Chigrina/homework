from collections import Counter

# from src.file_reader import path_to_csv_file, path_to_excel_file, read_csv_file, read_excel_file
# from src.utils import get_financial_transactions, path_to_file


def find_categories(transactions: list[dict], my_categories: list) -> dict:
    """
    Принимает список словарей с банковскими операциями и список категорий операций,
    возвращает словарь, в котором ключи - это название категорий, а значения - это количество операций
    в каждой категории
    """
    category_list = []

    for transaction in transactions:
        if transaction.get('description') in my_categories:
            category_list.append(transaction.get('description'))
    category_dict = dict(Counter(category_list))

    return category_dict


# if __name__ == '__main__':
#     trans = get_financial_transactions(path_to_file)
#     categories = ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет']
#     result = find_categories(trans, categories)
#     print(result)
#
# if __name__ == '__main__':
#     trans = read_csv_file(path_to_csv_file)
#     categories = ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет']
#     result = find_categories(trans, categories)
#     print(result)
#
#
# if __name__ == '__main__':
#     trans = read_excel_file(path_to_excel_file)
#     categories = ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет']
#     result = find_categories(trans, categories)
#     print(result)
