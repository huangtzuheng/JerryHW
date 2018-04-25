from django.db import models

# Create your models here.
class Person(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.CharField(max_length=15)
	hobby = models.CharField(max_length=100)
	facebook = models.CharField(max_length=50)
	email = models.CharField(max_length=50)

	def __str__(self):
		return self.name