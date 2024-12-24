from django.db import models # type: ignore
from django.utils.text import slugify # type: ignore


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50,default="",null=False,unique=True,db_index=True)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    imageurl = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=True)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False, blank=True, unique=True, db_index=True)
    categories = models.ManyToManyField(Category)


    def __str__(self):
        return f"{self.title}"
    
class UploadModel(models.Model):
   ## image = models.ImageField(upload_to="images")
   pass
        

    






    

