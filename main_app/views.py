from django.shortcuts import render, render_to_response
from datetime import date
from main_app.models import person, learningplaces, workplaces, hobbies



class Person(object):
	def __init__(self):
		ob = person.objects.get(pk=1)
		self.first_name = ob.name
		self.sacond_name = ob.middlename
		self.last_name = ob.surname
		self.age = ob.age
		self.hobbies = hobbies.objects.all()
		self.studies = learningplaces.objects.all()
		self.works = workplaces.objects.all()




# Create your views here.
def about_my(request):
	return render_to_response('about_my.html', {'person': Person()})

def study(request):
	return render_to_response('study.html', {'person': Person()})

def work(request):
	aa = 1
	return render_to_response('work.html', {'person': Person()})