from django.shortcuts import render,redirect
from .models import Signup
from django.contrib import messages
# Create your views here.
def public(request):
    return render(request,'public.html',)

def home(request):
    context = {'home':'active'}
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request,'home.html',context)

def about(request):
    context = {'about':'active'}
    return render(request,'about.html',context)
def contact(request):
    context = {'contact':'active'}
    return render(request,'contact.html',context)
def login(request):
    return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Signup.objects.get(email=email,)
            messages.info(request,'Account already exists! , Please Login.')
            return redirect('login')
        except :
            Signup.objects.create(email=email, password=password)
            messages.success(request,'SignUp Successful ! , Please Login.')
            return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Signup.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            messages.success(request,'Login Successful ! , Please try our services.')
            return redirect('home')
        except Signup.DoesNotExist:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('public')