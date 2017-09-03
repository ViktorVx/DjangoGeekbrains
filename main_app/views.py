from django.shortcuts import render, render_to_response
from main_app.models import Persons, Learning_places, Work_places, Hobbies, Sex



class Person(object):
	def __init__(self):
		ob = Persons.objects.get(pk=1)
		self.first_name = ob.name
		self.sacond_name = ob.middlename
		self.last_name = ob.surname
		self.age = ob.age
		self.sex = ob.sex.name
		self.hobbies = ob.hobbies.all()
		self.studies = ob.learning_places.all()
		self.works = ob.work_places.all()




# Create your views here.
def about_my(request):
	return render_to_response('about_my.html', {'person': Person()})

def study(request):
	return render_to_response('study.html', {'person': Person()})

def work(request):
	#Плохо!!!
	#Как подключать эти сраные виджеты!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	pr = Person()
	sh3 = True
	if sh3:
		pr.works = pr.works[:3]

	return render_to_response('work.html', {'person': pr})

def work_card(request, party):
	pr = Work_places.objects.get(pk=party)
	return render_to_response('work_card.html', {'wp':pr})