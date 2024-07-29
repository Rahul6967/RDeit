from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.conf import settings

def select_template(request):
    temps = Template.objects.all()
    return render(request,'afterlogin/select_temp.html',{'temps':temps}) 

def Userdetails(request, TempName):
    if request.method == 'POST':
        form = Userdetailform(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            userdata = Userdetailmodel.objects.create(
                fullname=cleaned_data['fullname'],
                role=cleaned_data['role'],
                phoneno=cleaned_data['phoneno'],
                email=cleaned_data['email'],
                address=cleaned_data['address'],
                dateofbirth=cleaned_data['dateofbirth'],
                profile=cleaned_data['profile'],
                education1=cleaned_data['education1'],
                institute1=cleaned_data['institute1'],
                education2=cleaned_data['education2'],
                institute2=cleaned_data['institute2'],
                education3=cleaned_data['education3'],
                institute3=cleaned_data['institute3'],
                skill1=cleaned_data['skill1'],
                skill2=cleaned_data['skill2'],
                skill3=cleaned_data['skill3'],
                skill4=cleaned_data['skill4'],
                skill5=cleaned_data['skill5'],
                skill6=cleaned_data['skill6'],
                experience1=cleaned_data['experience1'],
                experience2=cleaned_data['experience2'],
                description1=cleaned_data['description1'],
                description2=cleaned_data['description2'],
            )
            template_path = f'afterlogin/{TempName}.html'
            return render(request,template_path,{'userdata': userdata})

    else:
        form = Userdetailform()

    return render(request, 'afterlogin/userdetailform.html', {'form': form})


