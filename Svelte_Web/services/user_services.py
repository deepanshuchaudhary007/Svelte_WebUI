import json
import os
from dateutil import parser
import requests
from requests import session



#### Get Country From APis##########
def get_country():
    url = os.environ.get('USER_API')+"country/"
    res = requests.get(url)
    country = res.json()
    print(country)
    return country

######## Get States From Apis ####################
def get_state(id):
    url = os.environ.get('USER_API')+"state/"+str(id)
    res = requests.get(url)
    state = res.json()
    return state

######## Get City From Apis ####################
def get_city(id):
    city =[]  
    url = os.environ.get('USER_API')+"city/"+str(id)     
    res = requests.get(url)
    city = res.json()   
    return city

########## Service For User Login #########
def user_login(email, password):
    user_info = {'email': email, 'password': password}
    data = json.dumps(user_info)
    url = os.environ.get('USER_API')+"login/" 
    response = requests.post(url, json=data)
    res = response.json()  
    if res:      
        if res['message'] == 'Login Successfully':             
            return res
    return {}

def user_register(data):
    data = json.dumps(data)
    url = os.environ.get('USER_API')+"registeration/" 
    response = requests.post(url, json=data)
    return response

def user_profile(user_code):    
    url = os.environ.get('USER_API')+"profile/"+user_code 
    res = requests.get(url)
    response = res.json() 
    print(response)
    return response

def password_change(data, token):    
    data = json.dumps(data)
    url = os.environ.get('USER_API')+"change_password/" 
    response = requests.post(url, json=data, headers = {"Accept":"application/json", "Authorization": "Bearer "+token})
    res = response.json()     
    if res:       
        if res['message'] == 'Your password changed successfully': 
            print(res)            
            return res
    return {}

def link_for_forgot_password(data):
    data = json.dumps(data)
    url = os.environ.get('USER_API')+"forgot_password_link/" 
    response = requests.post(url, json=data,)
    res = response.json()  
    print(res)   
    if res: 
        if res['msg']=="Password Reset link generated":
            print(res)            
            return res
    return {}

def reset_password(data, uid, token): 
    data = json.dumps(data)
    url = os.environ.get('USER_API')+"forgot_password/"+uid+'/'+token 
    response = requests.post(url, json=data)
    res = response.json()     
    if res:       
        if res['message'] == 'Password Rest Successfully': 
            print(res)            
            return res
    return {}


def user_logout():
    url = os.environ.get('USER_API')+"logout/" 
    res =requests.get(url)
    print(res)
    return True

