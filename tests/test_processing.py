import pytest
from src.processing import filter_by_state, sort_by_date
from tests.conftest import dictionaries_4


def test_filter_by_state(dictionaries_1):
    assert filter_by_state(dictionaries_1, 'CANCELED') == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


def test_filter_by_state_no_state(dictionaries_2):
    assert filter_by_state(dictionaries_2, 'CANCELED') == []


def test_sort_by_date_ascending(dictionaries_1):
    assert  sort_by_date(dictionaries_1, False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
        ]


def test_sort_by_date_descending(dictionaries_1):
    assert  sort_by_date(dictionaries_1) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]


def test_sort_by_date_similar_date(dictionaries_3):
    assert  sort_by_date(dictionaries_3) == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2019-07-03T21:27:25.241689'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
        ]


def test_sort_by_date_empty(dictionaries_5):
    with pytest.raises(ValueError):
        sort_by_date(dictionaries_5)
