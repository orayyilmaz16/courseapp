from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('anasayfa')

def kurslar(request):
    return HttpResponse('kurs listesi')

def iletisim(request):
    return HttpResponse('iletisim')

def hakkimda(request):
    return HttpResponse('hakkımda')

