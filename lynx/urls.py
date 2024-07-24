from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_view, name='logout_'),
    path('article/<int:pk>/', views.one_article, name='article'),
]