from django.contrib import admin
from App.models import User,Category,Events,Gallary,Form

# Register your models here.
admin.site.register(User)
admin.site.register(Form)
admin.site.register(Category)
admin.site.register(Events)
admin.site.register(Gallary)