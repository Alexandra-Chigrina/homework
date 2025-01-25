import logging
import os.path

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    os.path.join(os.path.dirname(__file__), "..", "logs", "masks.log"), "w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску номера карты
    """
    str_card_number = str(card_number)
    logger.info("Выполняем проверку длины номера карты")
    if len(str_card_number) != 16:
        logger.error("Неверная длина номера карты")
        raise ValueError("Неверная длина номера карты")

    logger.info("Номер карты замаскирован")
    return f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску номера счета
    """
    str_account_number = str(account_number)
    logger.info("Проверяем длину номера счета")
    if len(str_account_number) != 20:
        logger.error("Неверная длина номера счета")
        raise ValueError("Неверная длина номера счета")

    logger.info("Номер счета замаскирован")
    return f"**{str_account_number[-4:]}"


# if __name__ == "__main__":
#     card_number_input = int(input())
#     print(get_mask_card_number(card_number_input))
#
#     account_number_input = int(input())
#     print(get_mask_account(account_number_input))
