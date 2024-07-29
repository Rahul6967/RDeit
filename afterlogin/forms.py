from django import forms
from datetime import datetime

class Userdetailform(forms.Form):
    fullname=forms.CharField(label='Full Name:',required=True,max_length=50,widget=forms.TextInput(attrs={'class': 'form-control dark'}))
    role=forms.CharField(label='Role:',max_length=50,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile=forms.CharField(label='Profile:',required=True,max_length=500,widget=forms.TextInput(attrs={'class': 'form-control'}))
    address=forms.CharField(label='Address:',max_length=500,widget=forms.TextInput(attrs={'class': 'form-control'}))
    dateofbirth=forms.DateField(label='Date Of Birth:',required=True,widget=forms.DateInput(attrs={'class': 'form-control','type': 'date'}))
    user_type_choices = [
        ('male', 'MALE'),
        ('female', 'FEMALE'),
        ('other', 'OTHER'),
    ]
    gender = forms.ChoiceField(label='Gender:',required=True,choices=user_type_choices, widget=forms.Select(attrs={'class': 'form-select'}))
    phoneno=forms.CharField(label='Phone No:',required=True,max_length=10,widget=forms.NumberInput(attrs={'class': 'form-control','type':'tel'}))
    email=forms.EmailField(label='Email:',required=True,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    skill1=forms.CharField(label='Skill 1:',max_length=20,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill2=forms.CharField(label='Skill 2:',max_length=20,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill3=forms.CharField(label='Skill 3:',max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill4=forms.CharField(label='Skill 4:',max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill5=forms.CharField(label='Skill 5:',max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    skill6=forms.CharField(label='Skill 6:',max_length=20,widget=forms.TextInput(attrs={'class': 'form-control'}))
    education1=forms.CharField(label='Education 1:',max_length=50,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    education2=forms.CharField(label='Education 2:',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    education3=forms.CharField(label='Education 3:',max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    institute1=forms.CharField(label='Institute:',max_length=100,required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))
    institute2=forms.CharField(label='Institute:',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    institute3=forms.CharField(label='Institute:',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience1=forms.CharField(label='Experience 1:',max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience2=forms.CharField(label='Experience 2:',max_length=30,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description1=forms.CharField(label='Description:',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
    description2=forms.CharField(label='Description:',max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))