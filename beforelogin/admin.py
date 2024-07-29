from django.contrib import admin
from .models import Signup

# Register your models here.
@admin.register(Signup)
class signupadmin(admin.ModelAdmin):
    list_display=('id','email')