from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.MusicianCreateView.as_view(), name='musician_create'),
    path('edit/<int:id>/', views.MusicianEditView.as_view(), name='edit_musician'),
    
]
