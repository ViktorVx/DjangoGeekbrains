from django.db import models

# Create your models here.

class Work_places(models.Model):
	name = models.CharField(max_length=128)
	translit = models.CharField(max_length=128, blank=True)
	year = models.DateField()
	full_info = models.CharField(max_length=1000, blank=True)
	def __str__(self):
		return self.name


class Hobbies(models.Model):
	name = models.CharField(max_length=128)
	year = models.DateField()
	main_hobby = models.BooleanField()
	def __str__(self):
		return self.name


class Learning_places(models.Model):
	name = models.CharField(max_length=128)
	year = models.DateField()
	def __str__(self):
		return self.name


class Persons(models.Model):
	name = models.CharField(max_length=128)
	surname = models.CharField(max_length=128)
	middlename = models.CharField(max_length=128)
	age = models.IntegerField()
	sex = models.ForeignKey('Sex')
	hobbies = models.ManyToManyField('Hobbies')
	work_places = models.ManyToManyField('Work_places')
	learning_places = models.ManyToManyField('Learning_places')
	children = models.ManyToManyField('self', blank=True)
	def __str__(self):
		return self.name + ' ' + self.surname


class Sex(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Politic(models.Model):
	person = models.OneToOneField(Persons, primary_key=True, on_delete=models.CASCADE)
	political_party = models.CharField(max_length = 256)
	political_philosophy = models.CharField(max_length = 256)