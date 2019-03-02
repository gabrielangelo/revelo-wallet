def format_error_payload(description, status):
    response = {
        'error': {
            'status':status, 
            'description':description
        }
    }
    return response 

def format_success_payload(data, status, success):
    response = {
        'data':data, 
        'status':status, 
        'success':success
    }

    return response 

def make_currency_tuple():
    from .constants import LIST_CURRENCY_TRANSACTIONS
    currency_choices = tuple(((LIST_CURRENCY_TRANSACTIONS[coin], coin)
         for coin in LIST_CURRENCY_TRANSACTIONS))     
    return currency_choices