from django.urls import path
from beforelogin import views

urlpatterns = [
    path('',views.public,name='public'),
    path('home/',views.home,name='home'),
    path("aboutus/",views.about,name="about"),
    path("contactus/",views.contact,name="contact"),
    path("login/",views.login_view,name="login"),
    path("signup/",views.signup,name="signup"),
    path("logout/",views.logout_view,name="logout"),
]
