from django.shortcuts import render,redirect
from django.http import HttpResponse
from App.forms import RegForm,ChpwdForm,UpPrf,Details,Worker
from django.contrib.auth.decorators import login_required
from App.models import User,Category,Events,Gallary,Form,Dash,Work
from django.core.mail import send_mail
from project import settings
from django.contrib import messages
from xhtml2pdf import pisa
from django.core.mail import EmailMessage
import tempfile
from django.template.loader import get_template
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger



def gallary(request):
	photo=Gallary.objects.all()
	return render(request,'html/gallary.html',{"photo":photo})

def events(request):
	dest=Events.objects.all()
	return render(request,'html/events.html',{"dest":dest})

def home(request):
	d=Category.objects.all()
	return render(request,'html/home.html',{'data':d})

def register(request):
	d=Category.objects.all()
	if request.method=="POST":
		q=RegForm(request.POST)
		if q.is_valid():
			q.save()
			return redirect('/lg')
	q=RegForm()
	return render(request,'html/register.html',{'u':q,'data':d})

def about(request):
	d=Category.objects.all()
	return render(request,'html/aboutus.html',{'data':d})

def dashboard(request):
	d=Category.objects.all()
	return render(request,'html/dashboard.html',{'data':d})


def contact(request):
	d=Category.objects.all()
	return render(request,'html/contact.html',{'data':d})


def profile(request):
	d=Category.objects.all()
	return render(request,'html/profile.html',{'data':d})

def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/lg')
	c=ChpwdForm(user=request)
	return render(request,'html/changepwd.html',{'t':c})

def showdata(req):
	
	return render(req,'html/showdata.html',{'wd':a,'info':b})

def view(req):
	
	return render(req,'html/view_details.html')

def updateprofile(request):
	if request.method == "POST":
		p=UpPrf(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/pf')
	p= UpPrf()
	return render(request,'html/updateprofile.html',{'e':p})


def user(request):
	if request.method =="POST":
		u=Details(request.POST)
		if u.is_valid():
			u.save()
			return redirect('/')
	u= Details()
	return render(request,'html/add_details.html',{'e':u})

def worker(request):
	if request.method =="POST":
		w=Worker(request.POST)
		if w.is_valid():
			w.save()
			return redirect('/')
	w= Worker()
	return render(request,'html/worker.html',{'e':w})

def worker_details(request):
	d=Work.objects.all()
	return render(request,'html/worker_details.html',{'dest':d})

@login_required
def donate(request):
	return render(request,'html/donate.html')

@login_required
def form(request):
	return render(request,'html/form.html')


def details(request):
	dest=Dash.objects.all()
	return render(request,'html/details.html',{"dest":dest})
