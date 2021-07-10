from django.urls import path
from App import views
from django.contrib.auth import views as ay

urlpatterns = [
	path('',views.home,name='hm'),
    path('ct',views.contact,name='ct'),
	path('db',views.dashboard,name='db'),
	path('lg/',ay.LoginView.as_view(template_name="html/login.html"),name="lgo"),
	path('reg/',views.register,name="rg"),
	path('abt/',views.about,name='at'),
	path('lgout/',ay.LogoutView.as_view(template_name='html/logout.html'),name="log"),
	path('pf/',views.profile,name='prf'),
	path('ch/',views.cgf,name="cg"),
	path('sd/',views.showdata,name="shd"),
    path('rst/',ay.PasswordResetView.as_view(template_name="html/resetpassword.html"),name="rt"),
    path('rst_done/',ay.PasswordResetDoneView.as_view(template_name="html/resetpassworddone.html"),name="password_reset_done"),
    path('rst_cf/<uidb64>/<token>/',ay.PasswordResetConfirmView.as_view(template_name="html/resetpasswordconfirm.html"),name="password_reset_confirm"),
    path('rst_cmplt/',ay.PasswordResetCompleteView.as_view(template_name="html/resetpwdcomplete.html"),name="password_reset_complete"),
    path('upf/',views.updateprofile,name='updatepf'),
	path('events/',views.events,name="events"), 
    path('gallary/',views.gallary,name="gallary"),
	path('user/',views.user,name="user"),
	path('donate/',views.donate,name="donate"),
	path('form/',views.form,name="form"),
	path('view/',views.view,name="view"),

    ]
