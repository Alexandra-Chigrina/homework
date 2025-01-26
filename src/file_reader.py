import os

import pandas as pd


def read_csv_file(path: str) -> list[dict]:
    """
    Принимает на вход путь до CSV-файла, возвращает список словарей с данными
    о финансовых транзакциях
    """
    try:
        if path.endswith(".csv"):
            df = pd.read_csv(path, delimiter=";")
            csv_data_dict = df.to_dict(orient="records")
            return csv_data_dict
        else:
            return []
    except FileNotFoundError:
        return []
    except Exception:
        return []


def read_excel_file(path: str) -> list[dict]:
    """
    Принимает на вход путь до EXCEL-файла, возвращает список словарей с данными
    о финансовых транзакциях
    """
    try:
        if path.endswith(".xlsx"):
            df = pd.read_excel(path)
            excel_data_dict = df.to_dict(orient="records")
            return excel_data_dict
        else:
            return []
    except FileNotFoundError:
        return []
    except Exception:
        return []


path_to_csv_file = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
path_to_excel_file = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")


# if __name__ == "__main__":
#     csv_result = read_csv_file(path_to_csv_file)
#     excel_result = read_excel_file(path_to_excel_file)
#     print(csv_result[:30])
#     print(excel_result[:30])
