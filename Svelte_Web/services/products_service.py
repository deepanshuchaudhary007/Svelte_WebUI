import json
import os
import requests

def get_all_category():
    url = os.environ.get('PRODUCTS_API')+"all_category/"
    res = requests.get(url)
    all_category = res.json()
    return all_category

def get_all_products():
    url = os.environ.get('PRODUCTS_API')+"all_product/"
    res = requests.get(url)
    all_products = res.json()
    print(all_products)
    return all_products

def products_details(slug):
    url = os.environ.get('PRODUCTS_API')+"product_details/"+slug
    res = requests.get(url)
    products_details = res.json()
    #print(products_details)
    return products_details

def product_on_category(slug):
    url = os.environ.get('PRODUCTS_API')+"product_on_category/"+slug
    res = requests.get(url)
    products_details = res.json()
    print(products_details)
    return products_details