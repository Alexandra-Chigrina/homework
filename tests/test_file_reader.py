from unittest.mock import patch

from src.file_reader import read_csv_file, read_excel_file
from src.utils import path_to_file


@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = [
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]
    data_dict = read_csv_file("test.csv")
    assert data_dict == [
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


@patch("pandas.read_csv")
def test_read_csv_empty(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = []
    data_dict = read_csv_file("test.csv")
    assert data_dict == []


def test_read_csv_not_csv():
    data_dict = read_csv_file(path_to_file)
    assert data_dict == []


@patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_read_csv_no_file(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = []
    data_dict = read_csv_file("test.csv")
    assert data_dict == []


@patch("pandas.read_csv", side_effect=Exception)
def test_read_csv_exception(mock_read_csv):
    mock_read_csv.return_value.to_dict.return_value = []
    data_dict = read_csv_file("test.csv")
    assert data_dict == []


@patch("pandas.read_excel")
def test_read_excel_file(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = [
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]
    data_dict = read_excel_file("test.xlsx")
    assert data_dict == [
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


@patch("pandas.read_excel")
def test_read_excel_empty(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = []
    data_dict = read_excel_file("test.xlsx")
    assert data_dict == []


def test_read_excel_not_excel():
    data_dict = read_excel_file(path_to_file)
    assert data_dict == []


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_read_excel_no_file(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = []
    data_dict = read_excel_file("test.xlsx")
    assert data_dict == []


@patch("pandas.read_excel", side_effect=Exception)
def test_read_excel_no_exception(mock_read_excel):
    mock_read_excel.return_value.to_dict.return_value = []
    data_dict = read_excel_file("test.xlsx")
    assert data_dict == []
