from django.contrib import admin
from django.urls import path,include

urlpatterns = [  # <--- Должно быть точно такое имя

    path('', include('users.urls')),
]