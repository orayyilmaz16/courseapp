
from django.forms import TextInput, Textarea  # type: ignore
from django import forms   # type: ignore
from courses.models import Course  

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Kurs Başlığı",
#         required=True,
#         error_messages={
#             "required": "kurs bağlığı girmelisiniz." }, 
#         widget=forms.TextInput(attrs={"class":"form-control"}))
    
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageurl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields =['title','description','imageurl','slug']
        labels = {
            'title': "Kurs Başlığı",
            'description': "Açıklama",
            'imageurl': "Resim Uzantısı",
            'slug': "Kod Adı"
        },
        widgets = {
            'title': TextInput(attrs={"class":"form-control"}),
            'description': Textarea(attrs={"class":"form-control"}),
            'imageurl': TextInput(attrs={"class":"form-control"}),
            'slug': TextInput(attrs={"class":"form-control"})

            
        }

