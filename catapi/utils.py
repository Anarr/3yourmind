def output(data, code=200):
    """
    Generate custom output from json data
    """
    
    return {
        'code': code,
        'data': data
    }

def modify_api_result(data):
    """
    modify catapi api result, remove unnecessary properties
    extract id and url fields from dictionary
    """
    data = [{'id': i['id'], 'url': i['url']} for i in data]

    return data