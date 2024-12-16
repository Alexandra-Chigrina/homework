import pytest
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('card_number, expected', [(5469040025684596, '5469 04** **** 4596'),
                                                   (4276325624256987, '4276 32** **** 6987'),
                                                   (2200254569854526, '2200 25** **** 4526')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_error():
    with pytest.raises(ValueError):
        get_mask_card_number(546904001256845)


def test_get_mask_card_number_empty():
    with pytest.raises(ValueError):
        get_mask_card_number('')


@pytest.mark.parametrize('account_number, expected', [(42706610004007525968, '**5968'),
                                                      (42705810004000025896, '**5896'),
                                                      (42695452689548532658, '**2658')])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_error():
    with pytest.raises(ValueError):
        get_mask_account(125654568521543658455)

def test_get_mask_account_empty():
    with pytest.raises(ValueError):
        get_mask_account('')
        