from src.utils import get_financial_transactions
from unittest.mock import patch, mock_open


@patch('builtins.open', new_callable=mock_open,
       read_data='[{"id": 441945886, "currency": "RUB", "amount": "31957.58"}]')
def test_get_financial_transactions(mock_file):
    fin_trans = get_financial_transactions('test.json')
    assert fin_trans == [{"id": 441945886, "currency": "RUB", "amount": "31957.58"}]
    mock_file.assert_called_once_with('test.json', 'r', encoding='utf-8')


@patch('builtins.open', new_callable=mock_open, read_data='')
def test_get_financial_transactions_empty(mock_file):
    fin_trans = get_financial_transactions('test.json')
    assert fin_trans == []


@patch('builtins.open', new_callable=mock_open,
       read_data='{"id": 441945886, "currency": "RUB", "amount": "31957.58"}')
def test_get_financial_transactions_incorrect(mock_file):
    fin_trans = get_financial_transactions('test.json')
    assert fin_trans == []


@patch('builtins.open', side_effect=FileNotFoundError)
def test_get_financial_transactions_not_found(mock_file):
    fin_trans = get_financial_transactions('test.json')
    assert fin_trans == []
