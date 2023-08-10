from django.contrib import admin
from .models import Breakfast,Lunch,Dinner

# Register your models here.

admin.site.register(Breakfast)
admin.site.register(Lunch)
admin.site.register(Dinner)