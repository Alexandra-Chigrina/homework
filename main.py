# from src.masks import get_mask_account, get_mask_card_number
# from src.processing import filter_by_state, sort_by_date
# from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.decorators import log

# from src.widget import get_date, mask_account_card

# card_number_input = int(input())
# print(get_mask_card_number(card_number_input))
#
#
# account_number_input = int(input())
# print(get_mask_account(account_number_input))
#
#
# # Maestro 1596837868705199
# # Счет 64686473678894779589
# # MasterCard 7158300734726758
# # Счет 35383033474447895560
# # Visa Classic 6831982476737658
# # Visa Platinum 8990922113665229
# # Visa Gold 5999414228426353
# # Счет 73654108430135874305
#
# print(mask_account_card("Счет 7365410843013587"))
#
#
# print(get_date("2024-03-11T02:26:18.671407"))


# example_of_dict = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
# print(filter_by_state(example_of_dict))
# print(sort_by_date(example_of_dict, False))

#
# transactions = (
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
# )
#
#
# usd_transactions = filter_by_currency(transactions, 'USD')
# for _ in range(3):
#     print(next(usd_transactions))
#
#
# descriptions = transaction_descriptions(transactions)
# for _ in range(5):
#     print(next(descriptions))
#
#
# for card_number in card_number_generator(8952458625865240, 8952458625865245):
#     print(card_number)


@log("mylog.txt")
# @log()
def my_function(x: int, y: int) -> float:
    return x / y


print(my_function(12, 0))
