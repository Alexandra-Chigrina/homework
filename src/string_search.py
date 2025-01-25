import re

from src.utils import get_financial_transactions, path_to_file
# from src.file_reader import read_csv_file, read_excel_file, path_to_excel_file, path_to_csv_file


def search_string_in_description(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Принимает список словарей с банковскими операциями и строку поиску, возвращает список словарей,
    у которых в описании есть данная строка
    """
    pattern = fr'\b{search_string}\b'
    new_trans_dict = []
    for transaction in transactions:
        if re.findall(pattern, str(transaction.get('description')), flags=re.IGNORECASE):
            new_trans_dict.append(transaction)

    return new_trans_dict


if __name__ == '__main__':
    trans = get_financial_transactions(path_to_file)
    result = search_string_in_description(trans, "Перевод")
    print(result)

# if __name__ == '__main__':
#     trans = read_csv_file(path_to_csv_file)
#     result = search_string_in_description(trans, "ПЕРЕВОД")
#     print(result)
#

# if __name__ == '__main__':
#     trans = read_excel_file(path_to_excel_file)
#     result = search_string_in_description(trans, "ПЕРЕВОД")
#     print(result)
