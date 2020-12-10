from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='orm-home'),
    path('about/', views.about, name='orm-about'),
]