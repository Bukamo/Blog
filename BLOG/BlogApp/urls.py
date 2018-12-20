from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='BlogApp-home'),
    path('about/', views.about, name='BlogApp-about'),

]
