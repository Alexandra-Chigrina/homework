def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты
    """
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        raise ValueError("Неверная длина номера карты")

    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера счета
    """
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        raise ValueError("Неверная длина номера счета")

    return f"**{str_account_number[-4:]}"
