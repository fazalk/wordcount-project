
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('/aboutme', views.aboutme, name='about'),
    path('count/', views.count, name='count'),
]
