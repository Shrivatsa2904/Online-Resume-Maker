from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='orm-home'),
      path('dashboard/', views.dashboard, name='orm-dashboard'),
    path('login/', views.loginpage, name='orm-login'),
      path('register/', views.register, name='orm-register'),
      path('logout/', views.logoutuser, name='orm-logout'),
       path('samples/', views.projectview, name='orm-sample'),
         path('internship/', views.internshipview, name='orm-internship'),
          path('certificate/', views.certificateview, name='orm-certificate'),
          path('choice/', views.choiceview, name='orm-choice'),
           path('pdf/', views.render_pdf, name='orm-pdf')

]