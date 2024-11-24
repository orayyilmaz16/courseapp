from datetime import date,datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Course
from .models import Category

data =  {
    "programlama": "programlama kategorisine ait kurslar",
    "web-geliştirme": "web geliştirme kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar",
    "mobil-uygulama": "mobil kategorisine ait kurslar"
}

db = {
    "courses": [
        {
            "title":"javascript kursu",
            "description":"javascript kurs açıklaması",
            "imageurl":"1.jpg",
            "slug":"javascript-kursu",
            "date": datetime.now,
            "isActive":True,
            "isUpdated": True,
        },
         {
            "title":"python kursu",
            "description":"python kurs açıklaması",
            "imageurl":"2.jpg",
            "slug":"python-kursu",
            "date": date(2022,9,10),
            "isActive":True,
            "isUpdated":True,
        },
         {
            "title":"web-geliştirme kursu",
            "description":"web-geliştirme kurs açıklaması",
            "imageurl":"3.jpg",
            "slug":"web-geliştirme-kursu",
            "date": date(2022,8,10),
            "isActive":True,
            "isUpdated":True,
        }
    ],
    "categories": [
       { "id":1, "name":"programlama","slug":"programlama"},
       { "id":2, "name":"web-geliştirme","slug":"web-geliştirme"},
       { "id":3, "name":"mobil-uygulamalar","slug":"mobil-uygulamalar"},
       
        
    ]
}

#http://127.0.0.1:8000/kurslar


def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()
    
  #  for kurs in db["courses"]:
  #      if kurs["isActive"] == True:
   #s         kurslar.append(kurs)
   
    return render(request,"courses/index.html",{
        'categories': kategoriler,
        "courses": kurslar,
    })


def details(request, kurs_id):
    # try:
        #  course = Course.objects.get(pk=kurs_id)
    # except:
        # raise Http404()
      
    course = get_object_or_404(Course, pk=kurs_id)
     
    context = {
        "course": course
    }
    return render(request,'courses/details.html',context)

def getCoursesByCategory(request, category_name):
    try:
       category_text = data[category_name]
       return render(request, 'courses/courses.html',{
           'category': category_name,
           'category_text': category_text,
       })
    except:
        return HttpResponseNotFound("<h1>yanlış kategori seçimi</h1>")

    

def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    
    category_name = category_list[category_id - 1] 
    

    redirect_url = reverse('courses_by_category', args=[category_name])

    return redirect(redirect_url)