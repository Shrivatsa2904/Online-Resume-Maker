from django.urls import path
from . import views

urlpatterns = [
      path('', views.home, name='orm-home'),
    path('login/', views.login, name='orm-login'),
      path('register/', views.register, name='orm-register')

]