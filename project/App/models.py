from django.db import models
from django.contrib.auth.models import User,AbstractUser
from datetime import date

class User(AbstractUser):
	t = (
		(1,'Admin'),
		(2,'Staff'),
		(3,"Donors"),
		)
	role = models.IntegerField(default=3,choices=t)
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

class Work(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=120)
	age=models.IntegerField()
	a=[('M',"Manager"),('W','Workers'),('A','Ass.Manager'),('s','Suppoters'),('o','Others')]
	qualification=models.CharField(max_length=10,choices=a,default="M")
	img =models.ImageField(upload_to='pics')	
	g=[('M',"Male"),('F','Female'),('O','Prefer not say')]
	gender=models.CharField(max_length=10,choices=g,default="M")
	phno=models.CharField(null='True',max_length=30)
	address =models.TextField(null='True')
	
class Form(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	age=models.IntegerField()
	image=models.ImageField(upload_to='pics')
	email=models.EmailField(max_length=120)
	fathername=models.CharField(max_length=50)
	fatheroccupation=models.CharField(max_length=25)
	g=[('M',"Male"),('F','Female'),('O','Prefer not say')]
	gender=models.CharField(max_length=10,choices=g,default="M")
	aadharno=models.CharField(null='True',max_length=12)
	phno=models.CharField(null='True',max_length=30)
	address=models.TextField(null='True')
	city=models.CharField(max_length=30,null='True')
	state=models.CharField(max_length=40,null='True')
	pin=models.IntegerField(null='True')
	a=[('i',"illiterate"),('s','Below 7th'),('t','10th'),('B','Above 10th'),('o','Higher Studies')]
	study=models.CharField(max_length=10,choices=a,default="s")

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

class Dash(models.Model):
	name=models.CharField(max_length=100)
	img =models.ImageField(upload_to='pics')
	des =models.TextField()
	