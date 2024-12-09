def filter_by_state(dict_list: list, state_value: str = 'EXECUTED') -> list:
    """
    Принимает список словарей и значение ключа 'state' (опционально - 'EXECUTED') и
    возвращает новый список словарей, содержащий словари с заданным ключом 'state'
    """
    new_dict_list = []
    for dictionary in dict_list:
        if dictionary.get('state') == state_value:
            new_dict_list.append(dictionary)
    return new_dict_list
