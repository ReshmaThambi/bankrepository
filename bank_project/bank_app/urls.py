from . import views
from django.urls import path
app_name = 'bank_app'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('welcome/', views.welcome, name='welcome'),
    path('form/', views.form, name='form'),
    path('msgbox/', views.msgbox, name='msgbox'),

]