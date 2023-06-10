import json
import os
import requests

def user_cart_id(user_code):    
    url = os.environ.get('CART_API')+"user_cart/"+user_code
    res = requests.get(url)
    if res:
        response = res.json()
        print(response)
    else:
        response = {}   
    return response

def get_cart_details(cart_id): 
    if cart_id is not None:  
        url = os.environ.get('CART_API')+"user_cart_items/"+cart_id
        print(url)
        res = requests.get(url)
        if res:
            response = res.json()
            print(response)
        else:
            response = {}   
        return response
    return {}

def cart_item_remove(id):
    if id is not None:  
        url = os.environ.get('CART_API')+"delete_cart_item/"+str(id)
        print(url)
        res = requests.delete(url)
        if res:
            response = res.json()
            print(response)
        else:
            response = {}   
        return response
    return {}
    
