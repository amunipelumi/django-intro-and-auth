from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('article/<int:pk>/', views.one_article, name='article'),
]