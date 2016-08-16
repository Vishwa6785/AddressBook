from django.db import models
from django.contrib import admin

# Create your models here.

class Address(models.Model):
	name = models.CharField(max_length=10)
	email = models.CharField(max_length=20,primary_key=True)
	age = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
 		#return self.name
 		return u' %s %s' %(self.name, self.email)


admin.site.register(Address)