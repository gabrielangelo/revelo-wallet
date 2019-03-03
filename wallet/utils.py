def make_currency_tuple():
    from .constants import LIST_CURRENCY_TRANSACTIONS
    currency_choices = tuple(((LIST_CURRENCY_TRANSACTIONS[coin], coin)
        for coin in LIST_CURRENCY_TRANSACTIONS))     
    return currency_choices