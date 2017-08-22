from django.shortcuts import render, render_to_response



class Person(object):
	def __init__(self):
		self.first_name = 'Иван'
		self.sacond_name = 'Иванович'
		self.last_name = 'Иванов'
		self.birthdate = '30 августа 1978 года'
		self.hobby = 'Люблю программировать на Питоне!'




# Create your views here.
def about_my(request):
	return render_to_response('about_my.html', {'person': Person()})

def study(request):
	return render_to_response('study.html')

def work(request):
	return render_to_response('work.html')