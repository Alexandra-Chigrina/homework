def filter_by_state(dict_list: list, state_value: str = "EXECUTED") -> list:
    """
    Принимает список словарей и значение ключа 'state' (опционально - 'EXECUTED') и
    возвращает новый список словарей, содержащий словари с заданным ключом 'state'
    """
    new_dict_list = []
    for dictionary in dict_list:
        if dictionary.get("state") == state_value:
            new_dict_list.append(dictionary)
    return new_dict_list


def sort_by_date(dict_list: list, reverse_value: bool = True) -> list:
    """
    Принимает список словарей и параметр, задающий параметр сортировки (по умолчанию - убывание),
    и возвращает новый список, отсортированный по дате
    """
    sorted_dict_list = sorted(dict_list, key=lambda dictionary: dictionary["date"], reverse=reverse_value)
    return sorted_dict_list
