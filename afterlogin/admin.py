from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Template)
class Templates(admin.ModelAdmin):
    list_display=('TempName','Description')
@admin.register(Userdetailmodel)
class Userdetails(admin.ModelAdmin):
    list_display=('fullname','role','gender','phoneno')