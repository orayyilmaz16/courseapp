
from django.forms import SelectMultiple, TextInput, Textarea  # type: ignore
from django import forms   # type: ignore
from courses.models import Course  



class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =('title','description','imageurl','slug','categories','isActive')
        labels = {
            'title': "Kurs Başlığı",
            'description': "Açıklama",
            'imageurl': "Resim Uzantısı",
            'slug': "Kod Adı",
            'categories': "Kategori Adı",
            'isActive': 'Ana sayfada gözüksün mü?'
            
        }
        widgets = {
            'title': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"}),
            'imageurl': TextInput(attrs={"class":"form-control"}),
            'slug': TextInput(attrs={"class":"form-control"}),
            'categories': SelectMultiple(attrs={"class":"form-control"}),
            
            
        }
        error_messages = {

            "title": {
            "required": "kurs bağlığı girmelisiniz.",
            "max_length": "maksimum 50 karakter girmelisiniz"
            },

            "description": {
                "required": "kurs açıklaması gereklidir."
            }
         
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =('title','description','imageurl','slug','categories','isActive')
        labels = {
            'title': "Kurs Başlığı",
            'description': "Açıklama",
            'imageurl': "Resim Uzantısı",
            'slug': "Kod Adı",
            'categories': "Kategori"
            
        }
        widgets = {
            'title': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"}),
            'imageurl': TextInput(attrs={"class":"form-control"}),
            'slug': TextInput(attrs={"class":"form-control"}),
            'categories': SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {

            "title": {
            "required": "kurs bağlığı girmelisiniz.",
            "max_length": "maksimum 50 karakter girmelisiniz"
            },

            "description": {
                "required": "kurs açıklaması gereklidir."
            }
         
        }


class UploadForm(forms.Form):
    image = forms.ImageField()
        
        
        

