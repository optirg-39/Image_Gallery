from django.urls import path
from . import views
urlpatterns = [
    path('addphoto/', views.addPhoto, name = 'addPhoto'),
    path('', views.albumgallery, name = 'gallery'),
    path('photo/<int:pk>', views.albumphoto, name = 'photose'),
]
