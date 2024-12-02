from src.masks import get_mask_account, get_mask_card_number

card_number_input = int(input())
print(get_mask_card_number(card_number_input))


account_number_input = int(input())
print(get_mask_account(account_number_input))
