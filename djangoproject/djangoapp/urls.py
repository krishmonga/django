# djangoapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chai/', views.chai, name='chai'),
    path('chai/<int:chai_id>/', views.chai_detail, name='chai_detail'),
]
