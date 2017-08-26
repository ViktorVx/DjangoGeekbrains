from django.shortcuts import render, render_to_response
from datetime import date



class Person(object):
	def __init__(self):
		self.first_name = 'Владимир'
		self.sacond_name = 'Ильич'
		self.last_name = 'Ленин'
		self.birthdate = date(1870, 4, 10)
		self.hobby = 'Социалистическая революция'
		self.studies = ['Симбирская гимназия','Казанский университет']
		self.works = ['председатель Совета Народных Комиссаров СССР',\
					'председатель Совета Народных Комиссаров РСФСР', \
					'1-й председатель Совета Труда и Обороны СССР',\
					'Член Политбюро ЦК РКП(б)',\
					'Член Политбюро ЦК РСДРП(б)']
		#self.studies = []
		#self.works = []



# Create your views here.
def about_my(request):
	return render_to_response('about_my.html', {'person': Person()})

def study(request):
	return render_to_response('study.html', {'person': Person()})

def work(request):
	aa = 1
	return render_to_response('work.html', {'person': Person()})