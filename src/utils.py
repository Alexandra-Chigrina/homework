import json
import os.path


def get_financial_transactions(path: str) -> list[dict] :
    """
    Принммает на вход путь до JSON-файла, возвращает список словарей с данными
    о финансовых транзакциях
    """

    try:
        with open(path, 'r', encoding='utf-8') as file:
            try:
                transactions = json.load(file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


path_to_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json')


# if __name__ == '__main__':
#     result = get_financial_transactions(path_to_file)
#     print(result)
