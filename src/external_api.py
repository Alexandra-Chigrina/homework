import requests
import os
from dotenv import load_dotenv
# from src.utils import get_financial_transactions, path_to_file


load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_transaction_amount(transaction: dict) -> float | None:
    """
    Принимает транзакцию, возвращает сумму транзакции в рублях
    """

    currency_code = transaction['operationAmount']['currency']['code']
    trans_amount = float(transaction['operationAmount']['amount'])

    if currency_code == 'RUB':
        return trans_amount

    else:
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={trans_amount}'
        headers = {'apikey': f'{API_KEY}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            currency_data = response.json()
            currency_amount = float(currency_data['result'])

        else:
            raise ValueError(f"Failed to get the currency rate. Status code: {response.reason}.")

        return currency_amount


# if __name__ == '__main__':
#     transaction = get_financial_transactions(path_to_file)[1]
#     result = get_transaction_amount(transaction)
#     print(result)
