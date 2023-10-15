from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Student)
from rest_framework import routers, serializers, viewsets
from .models import *
class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       model=Student
       fields="__all__"