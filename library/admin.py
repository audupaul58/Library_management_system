from django.contrib import admin
from .models import *
BookIssued
admin.site.register(Book)
admin.site.register(Student)
admin.site.register(IssuedBook)
admin.site.register(BookIssued)