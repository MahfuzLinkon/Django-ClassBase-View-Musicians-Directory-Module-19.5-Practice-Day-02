from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.AlbumCreateView.as_view(), name='album_create'),
    path('edit/<int:id>/', views.AlbumEditView.as_view(), name='edit_album'),
    path('delete/<int:id>/', views.AlbumDeleteView.as_view(), name='delete_album'),
]