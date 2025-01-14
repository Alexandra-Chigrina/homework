from src.external_api import get_transaction_amount
from src.utils import get_financial_transactions, path_to_file
from unittest.mock import patch, Mock
import pytest


def test_get_trans_amount_RUB():
    transaction = get_financial_transactions(path_to_file)[0]
    assert get_transaction_amount(transaction) == 31957.58


def test_get_transaction_amount():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "from": "USD",
        "to": "RUB",
        "amount": 8221.37,
        "rate": 103.369018,
        "result": 849834.943515
    }

    with patch('requests.get', return_value=mock_response):
        test_transaction = {'id': 41428829,
                            'state': 'EXECUTED',
                            'date': '2019-07-03T18:35:29.512364',
                            'operationAmount': {'amount': '8221.37',
                                                'currency': {'name': 'USDT', 'code': 'USD'}}}
        result = get_transaction_amount(test_transaction)
        assert result == 849834.943515


def test_get_trans_amount_no_currency():
    mock_response = Mock()
    mock_response.status_code = 400

    with patch('requests.get', return_value=mock_response):
        with pytest.raises(ValueError):
            test_transaction = {'id': 41428829,
                                'state': 'EXECUTED',
                                'date': '2019-07-03T18:35:29.512364',
                                'operationAmount': {'amount': '132.47',
                                                    'currency': {'name': 'USDT', 'code': 'USDT'}}}
            get_transaction_amount(test_transaction)
