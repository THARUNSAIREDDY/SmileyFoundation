from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from App.models import User,Category,Gallary,Events,Form,Work

class RegForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"enter password",
		"id":"pswd1" 
		}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={
		"class":"form-control",
		"placeholder":"confirm password",
		"id":"pswd2"
		}))
	class Meta:
		model=User
		fields=['username','email']
		widgets ={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter username",
			"id":"name"
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"enter email",
			})
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']

class UpPrf(forms.ModelForm):
	class Meta:
		model= User
		fields = ["address","email","phno","city","state","pin","image"]
		widgets = {
		"address":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"address"}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter your email"}),
		"phno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),
		"city":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"city"}),
		"state":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"state"}),
		"pin":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Pincode"}),
		}

class Details(forms.ModelForm):
	
	class Meta:
		model= Form
		fields = ["first_name","last_name","age","image","email","study","gender","aadharno","phno","fathername","fatheroccupation","address","city","state","pin"]
		widgets = {
		"first_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter your First name "}),
		"last_name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter your Last name "}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter  your age:",}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter your Email"}),
		"study":forms.Select(attrs={"class":"form-control my-2","placeholder":"select your qualification"}),
		"fathername":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter your Father name "}),
		"fatheroccupation":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter Father's occupation"}),
		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Select your gender",}),
		"aadharno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Aadhar number"}),
		"phno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),
		"address":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"address"}),
		"city":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"city"}),
		"state":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"state"}),
		"pin":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Pincode"}),
		}

class Worker(forms.ModelForm):
	
	class Meta:
		model= Work
		fields = ["name","age","email","qualification","img","gender","phno","address"]
		widgets = {
		"name":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Enter your Name "}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter  your age:",}),
		"email":forms.EmailInput(attrs={"class":"form-control my-2","placeholder":"Enter your Email"}),
		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Select your gender",}),
		"qualification":forms.Select(attrs={"class":"form-control","placeholder":"Select your Qualification",}),
		"phno":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"Phone number"}),
		"address":forms.TextInput(attrs={"class":"form-control my-2","placeholder":"address"}),
		}
