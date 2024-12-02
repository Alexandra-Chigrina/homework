from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(user_data: str) -> str:
    """
    Возвращает строку с замаскированным номером
    """
    user_data_list = user_data.split()
    if len(user_data_list[-1]) == 16:
        return user_data[:-16] + get_mask_card_number(int(user_data_list[-1]))
    elif len(user_data_list[-1]) == 20:
        return user_data[:-20] + get_mask_account(int(user_data_list[-1]))




