# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#photo = models.ImageField(upload_to="gallery")
class Customer(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.IntegerField()
	adress=models.CharField(max_length=500)
	Date=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.adress

class Buy(models.Model):
	user=models.CharField(max_length=23)
	product_details=models.CharField(max_length=500)
	quantity=models.IntegerField()
	Date=models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.quantity

class Sell(models.Model):
	user=models.CharField(max_length=23)
	product_details=models.CharField(max_length=500)
	quantity=models.IntegerField()
	price=models.IntegerField()
	Date=models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.quantity



