import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "user_data, expected",
    [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(user_data, expected):
    assert mask_account_card(user_data) == expected


def test_mask_account_card_error():
    with pytest.raises(ValueError):
        mask_account_card("MasterCard 715830073472675")


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2020-12-31T04:36:40.658495", "31.12.2020"),
        ("2023-01-01T08:05:22.671407", "01.01.2023"),
    ],
)
def test_get_date(date, expected):
    assert get_date(date) == expected


def test_get_date_error():
    with pytest.raises(ValueError):
        get_date("T02:26:18.671407")


def test_get_date_empty():
    with pytest.raises(ValueError):
        get_date("")
