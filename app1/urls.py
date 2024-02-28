# from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('', newhomepage, name='newhomepage'),
    path('travelpackage/', travelpackage, name='travelpackage'),
    path('print1/', print1, name='print1'),
    path('print_to_console/',print_to_console, name='print_to_console'),
    path('randomcall/',randomcall, name = 'randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('pie_chart/', pie_chart, name = 'pie_chart'),
    path('car/', car, name='car'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('weatherpagecall/', weatherpagecall, name='weatherpagecall'),
    path('myregisterpage1/', myregisterpage1, name='myregisterpage1'),
    path('registerloginfunction/',registerloginfunction , name='registerloginfunction'),
    path('login/',login, name='login'),
    path('signup',signup,name='signup'),

]
