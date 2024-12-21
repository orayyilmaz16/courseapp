from django.contrib import admin # type: ignore
from .models import Course

admin.site.register(Course)
