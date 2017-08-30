from django.db import models

# Create your models here.
class workplaces(models.Model):
	name = models.CharField(max_length=128)
	year = models.DateField()
	def __str__(self):
		return self.name


class hobbies(models.Model):
	name = models.CharField(max_length=128)
	year = models.DateField()
	main_hobby = models.BooleanField()
	def __str__(self):
		return self.name


class learningplaces(models.Model):
	name = models.CharField(max_length=128)
	year = models.DateField()
	def __str__(self):
		return self.name


class person(models.Model):
	name = models.CharField(max_length=128)
	suranme = models.CharField(max_length=128)
	middlename = models.CharField(max_length=128)
	age = models.IntegerField()
	def __str__(self):
		return self.name + ' ' + self.surname

