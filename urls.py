from django.contrib import admin
from django.urls import path
from Application import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('Home', views.Home, name='home'),
    path('About',views.About, name='about'),
    path('Contact', views.Contact, name='contact'),
    path('Merit', views.Merit, name='merit'),
    path('Athletic', views.Athletic, name='athletic'),
    path('Economical', views.Economical, name='economical'),
    path('Login', views.Login, name='login'),
    path('Logout', views.LogoutUser, name='logout'),
    path('Meritservice',views.Mservice,name='mservice'),
    path('Sportservice',views.Sservice, name='sservice'),
    path('Economicalservice',views.Eservice,name='eservice')
]
