from django.shortcuts import render, render_to_response
from datetime import date



class Person(object):
	def __init__(self):
		self.first_name = 'Иван'
		self.sacond_name = 'Иванович'
		self.last_name = 'Иванов'
		self.birthdate = date(1978, 8, 30)
		self.hobby = 'Люблю программировать на Питоне!'
		#self.studies = ['СОШ № 38 г. Волгограда','Институт изучения внеземных цивилизаций имени Анунака', 'СПБГТФХУ']
		#self.works = ['ОАО Звездочка','ОАО ПолимерБытПромТехнология', 'ООО ЗверьШкурПром']
		self.studies = []
		self.works = []



# Create your views here.
def about_my(request):
	return render_to_response('about_my.html', {'person': Person()})

def study(request):
	return render_to_response('study.html', {'person': Person()})

def work(request):
	aa = 1
	return render_to_response('work.html', {'person': Person()})