
# Create your models here.

from django.db import models

# Create your models here.
class Category(models.Model):
	types	 = models.CharField(max_length=100)
	timestamp= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.types





class Menu_model(models.Model):
	category = models.ForeignKey('category')
	time     = models.DateTimeField(auto_now_add=True)
	name     = models.CharField(max_length=100)
	price    = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

	
