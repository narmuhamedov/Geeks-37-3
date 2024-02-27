from django.urls import path
from . import views

urlpatterns = [
    path('news_list/', views.news_list, name='news'),
]