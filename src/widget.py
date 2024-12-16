from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:
    """
    Возвращает строку с замаскированным номером
    """
    user_data_list = user_data.split()
    if len(user_data_list[-1]) == 16:
        return user_data[:-16] + get_mask_card_number(int(user_data_list[-1]))
    elif len(user_data_list[-1]) == 20:
        return user_data[:-20] + get_mask_account(int(user_data_list[-1]))
    else:
        raise ValueError("Неверная длина номера карты/счета")


def get_date(date_data: str) -> str:
    """
    Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'
    """
    if len(date_data) != 26:
        raise ValueError('Неверный формат данных')
    return f"{date_data[8:10]}.{date_data[5:7]}.{date_data[0:4]}"



