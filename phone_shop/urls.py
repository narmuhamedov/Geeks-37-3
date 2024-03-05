from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhoneShopView.as_view(), name='phone_list'),
    path('phone_detail/<int:id>/', views.PhoneShopDetailView.as_view(), name='phone_detail'),
    path('phone_detail/<int:id>/delete/', views.DeletePhoneView.as_view(), name='phone_delete'),
    path('phone_detail/<int:id>/update/', views.UpdatePhoneView.as_view(), name='update_phone'),
    path('create_phone/', views.CreatePhoneView.as_view(), name='create_phone'),
    path('seach/', views.SearchView.as_view(), name='search'),
    path('good/', views.good_request, name='good_request'),
]