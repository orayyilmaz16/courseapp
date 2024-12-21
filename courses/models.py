from django.db import models # type: ignore
from django.utils.text import slugify # type: ignore



class Course(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField()
    imageurl = models.CharField(max_length=50, blank=False)
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(default="",null=False, blank=True, unique=True, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)


    def __str__(self):
        return f"{self.title}"
        

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"





    

