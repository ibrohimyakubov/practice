from django.urls import path
from photos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category-phosts/<int:pk>/', views.category_photos, name='category-photos'),
    path('photos-detail/<int:pk>/', views.photos_detail, name='photos-detail'),
    path('search/', views.search, name='search'),
]
