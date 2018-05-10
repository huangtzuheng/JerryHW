from django.db import models

# Create your models here.
class Message(models.Model):
	username = models.CharField(max_length=200)
	#pub_date = models.DateTimeField('date published')
	title = models.CharField(max_length=200)
	content = models.CharField(max_length=500)
	#publish = models.DateTimeField()

	#def __str__(self):
    	#return self.user_name + "(" + self.publish.strftime('%Y-%m-%d %H:%M') + ") : " + self.title