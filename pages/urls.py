from django.urls import path
from . import views

#http://127.0.0.1:8000/client => anasayfa
#http://127.0.0.1:8000/client/home => anasayfa
#http://127.0.0.1:8000/client/kurslar => kurs listesi
#http://127.0.0.1:8000/client/kurslar




urlpatterns = [
    path('',views.index),
    path('index', views.index),
    path('contact',views.contact),
    path('about',views.about),
]
