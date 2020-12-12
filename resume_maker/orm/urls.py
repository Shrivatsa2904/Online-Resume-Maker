from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='orm-home'),
      path('dashboard/', views.dashboard, name='orm-dashboard'),
    path('login/', views.loginpage, name='orm-login'),
      path('register/', views.register, name='orm-register'),
      path('logout/', views.logoutuser, name='orm-logout')

]