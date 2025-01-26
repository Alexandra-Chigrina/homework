from src.utils import get_financial_transactions, path_to_file
from src.file_reader import read_csv_file, read_excel_file, path_to_csv_file, path_to_excel_file
from src.processing import filter_by_state, sort_by_date
from src.string_search import search_string_in_description
from src.masks import get_mask_account, get_mask_card_number
from typing import Any


def get_account_data(trans: dict) -> str:
    if str(trans["from"]) == 'nan':
        del trans["from"]
    if str(trans["to"]) == 'nan':
        del trans["to"]

    if trans.get("from"):
        from_account = str(trans.get("from")).split()
        if from_account[0].lower() == 'счет':
            from_data = f"{" ".join(from_account[0:-1])} {get_mask_account(from_account[-1])} -> "
        else:
            from_data = f"{" ".join(from_account[0:-1])} {get_mask_card_number(from_account[-1])} -> "
    else:
        from_data = ""

    if trans.get("to"):
        to_account = str(trans.get("to")).split()
        if to_account[0].lower() == 'счет':
            to_data = f"{" ".join(to_account[0:-1])} {get_mask_account(to_account[-1])}"
        else:
            to_data = f"{" ".join(to_account[0:-1])} {get_mask_card_number(to_account[-1])}"
    else:
        to_data = ""

    return f"{from_data}{to_data}"


def main() -> Any:

    print(
        "Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла.
    2. Получить информацию о транзакциях из CSV-файла.
    3. Получить информацию о транзакциях из XLSX-файла."""
    )

    # пользователь выбирает файл для обработки
    file_type_input = input()
    transactions_data = []
    while file_type_input not in ["1", "2", "3"]:
        file_type_input = input("Введен некорректный номер. Попробуйте снова: ")

    if file_type_input == "1":
        print("Для обработки выбран JSON-файл.")
        transactions_data = get_financial_transactions(path_to_file)
    if file_type_input == "2":
        print("Для обработки выбран CSV-файл.")
        transactions_data = read_csv_file(path_to_csv_file)
    if file_type_input == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions_data = read_excel_file(path_to_excel_file)

    # пользователь выбирает статус интересующих его операций
    state_input = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
    ).upper()
    while state_input not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {state_input} недоступен")
        state_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        ).upper()

    filtered_transactions = filter_by_state(transactions_data, state_input)

    # пользователь отвечает на уточняющие вопросы
    # # 1 вопрос. Сортировка операции по дате.
    date_sorting_input = input("Отсортировать операции по дате? Да/Нет: ").lower()

    while date_sorting_input not in ["да", "нет"]:
        date_sorting_input = input("Отсортировать операции по дате? Да/Нет: ").lower()

    if date_sorting_input == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        date_sorting_type = input("По возрастанию/по убыванию: ").lower()
        while date_sorting_type not in ["по возрастанию", "по убыванию"]:
            print("Отсортировать по возрастанию или по убыванию?")
            date_sorting_type = input("По возрастанию/по убыванию: ").lower()

        if date_sorting_type == "по возрастанию":
            filtered_transactions = sort_by_date(filtered_transactions, reverse_value=False)
        elif date_sorting_type == "по убыванию":
            filtered_transactions = sort_by_date(filtered_transactions)

    # # 2 вопрос. Фильтрация операций по RUB.
    trans_currency_input = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    while trans_currency_input not in ["да", "нет"]:
        trans_currency_input = input("Выводить только рублевые транзакции? Да/Нет: ")
    if trans_currency_input == "да":
        if file_type_input == "1":
            rub_trans = \
                [trans for trans in filtered_transactions if trans["operationAmount"]["currency"]["code"] == "RUB"]

        else:
            rub_trans = [trans for trans in filtered_transactions if trans["currency_code"] == "RUB"]
        filtered_transactions = rub_trans

    # 3 вопрос. Фильтрация по определенному слову в описании
    filter_description_input = input("Отфильтровать список транзакций по определенному слову в описании?\n"
                               "Да/Нет: ").lower()
    while filter_description_input not in ["да", "нет"]:
        filter_description_input = input("Отфильтровать список транзакций по определенному слову в описании?\n"
                                         "Да/Нет: ").lower()
    if filter_description_input == "да":
        search_word= input("Введите слово, по которому будет происходить фильтрация: ")
        if not filtered_transactions:
            filtered_transactions = []
        else:
            filtered_transactions = search_string_in_description(filtered_transactions, search_word)

    print("Распечатываю итоговый список транзакций...")
    if len(filtered_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
    else:
        print(f"Всего банковский операций в выборке: {len(filtered_transactions)}\n")

        for trans in filtered_transactions:
            date_data = trans.get("date")
            trans_date = f"{date_data[8:10]}.{date_data[5:7]}.{date_data[0:4]}"
            from_to_accounts = get_account_data(trans)
            if file_type_input == "1":
                trans_amount = trans["operationAmount"]["amount"]
                trans_currency = trans["operationAmount"]["currency"]["code"]
            else:
                trans_amount = trans["amount"]
                trans_currency = trans["currency_code"]

            print(f"{trans_date} {trans.get("description")}\n"
                  f"{from_to_accounts}\n"
                  f"Сумма: {trans_amount} {trans_currency}\n")


if __name__ == "__main__":
    result = main()
    print(result)
