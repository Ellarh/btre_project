from django.urls import path

from . import views

urlpatterns =[
    # This consist of the path. The first is the route, the second is the method name and the third is just the name you use when you want to link to the particular page
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),

]
