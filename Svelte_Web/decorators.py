import datetime
from dateutil import parser
from django.http import HttpResponseRedirect
from requests import session


# def login_requirs(function):
#     def wrapper(request, *args, **kw):
#         login_at = parser.parse(session['login_at'])
#         current_time = datetime.datetime.now() 
#         login_time = login_at - current_time
#         minutes = login_time.total_seconds() / 60
#         if minutes > 15:
#             return HttpResponseRedirect('/login/')
#         else:
#             return function(request, *args, **kw)
    

def required_login(function):
	def wraper(request, *args, **kwargs): 
		if 'login_time' in request.session:               
			if (((datetime.datetime.now()) - (parser.parse(request.session['login_time'])) ).total_seconds() / 60) > 15:
				del request.session['login_time']  
				del request.session['user_name']             
				return HttpResponseRedirect("/login/")
			else:
				request.session['login_time'] = str(datetime.datetime.now())
				return function(request, *args, **kwargs)
		else:
			return function(request, *args, **kwargs)	
        
	# wraper.__doc__=function.__doc__
	# wraper.__name__=function.__name__
	return wraper