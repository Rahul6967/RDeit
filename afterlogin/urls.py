from django.urls import path
from afterlogin import views


urlpatterns = [
    path('select-template/',views.select_template,name='select_template'),
    path('user-detail/<str:TempName>/',views.Userdetails,name='userdetailform'),
]

