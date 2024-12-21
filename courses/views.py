from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render # type: ignore
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect # type: ignore
from django.urls import reverse # type: ignore
from .models import Course
from .models import Category
from django.core.paginator import Paginator  # type: ignore


#http://127.0.0.1:8000/kurslar


def index(request):
    kurslar = Course.objects.all()
    kategoriler = Category.objects.all()
    
  #  for kurs in db["courses"]:
  #      if kurs["isActive"] == True:
   #s         kurslar.append(kurs)
   
    return render(request,"courses/index.html",{
        'categories': kategoriler,
        "courses": kurslar,
    })


def details(request, slug):
        
    course = get_object_or_404(Course, slug=slug)
     
    context = {
        "course": course
    }
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 1)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

   
    return render(request, 'courses/index.html',{
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })
