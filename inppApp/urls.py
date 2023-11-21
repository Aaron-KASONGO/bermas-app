from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sous-reseaux/<int:id>', views.sous_reseaux, name='sous-reseaux'),
    path('equipment/<int:id>', views.equipment, name='equipment'),
    path('run-putty/<str:ip>', views.open_putty, name='open-putty')
]
