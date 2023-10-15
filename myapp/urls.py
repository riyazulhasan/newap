from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns=[
    
    path('get/students/',api),
    path('student/',post_student),
    path('up_student/<id>/',update_student),
    path('de_student/<id>/',delete_student),
]