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