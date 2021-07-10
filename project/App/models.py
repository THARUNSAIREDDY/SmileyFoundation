from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date

class User(AbstractUser):
	image=models.ImageField(upload_to='profiles/',default="profile.jpg")
	email=models.EmailField(max_length=120)
	phno=models.CharField(null='True',max_length=30)
	address=models.TextField(null='True')
	city=models.CharField(max_length=30,null='True')
	state=models.CharField(max_length=40,null='True')
	pin=models.IntegerField(null='True')
	

	# nameoncard=models.CharField(max_length=30,null='True')
	# creditcardnumber=models.IntegerField(null='True')
	# Expyear=models.DateField(null='True')
	# expmonth=models.CharField(max_length=20,null='True')
	# cvv=models.IntegerField(null='True')s
	# t = (
	# 	(1,''),
	# 	(2,'Anonymous'),
	# 	)
	# role = models.IntegerField(default=1,choices=t)
	
class Form(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	image=models.ImageField(upload_to='profiles/',default="profile.jpg")
	email=models.EmailField(max_length=120)
	fathername=models.CharField(max_length=50)
	fatheroccupation=models.CharField(max_length=25)
	g=[('M',"Male"),('F','Female'),('O','Others')]
	gender=models.CharField(max_length=10,choices=g,default="M")
	age=models.IntegerField(default=10)
	aadharno=models.CharField(null='True',max_length=12)
	phno=models.CharField(null='True',max_length=30)
	address=models.TextField(null='True')
	city=models.CharField(max_length=30,null='True')
	state=models.CharField(max_length=40,null='True')
	pin=models.IntegerField(null='True')
	
	

class Category(models.Model):
	cname=models.CharField(max_length=20)
	def __str__(self):
		return self.cname

class Events(models.Model):
	name=models.CharField(max_length=100)
	img =models.ImageField(upload_to='pics')
	des =models.TextField()

class Gallary(models.Model):
	img =models.ImageField(upload_to='pics')


	