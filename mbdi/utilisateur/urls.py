from django.urls import path
from utilisateur.views import *


urlpatterns = [
    path('register',register , name='register'),
    path('login',user_login , name='login'),
    path('logout',user_logout , name='logout'),
    path('', Viewdata, name="home"),
    path('getdata', getdata, name='getdata'),
    path('form', create, name='create'),
    path('delete/<int:my_id>', deleteUser, name='delete'),
    path('getdatabis', getdatabis, name="getdatabis"),
    path('active', ViewdataBis, name="active"),
    path('deleteact/<int:my_id>', deleteUseract, name='deleteact'),
    path('deletecurent/<int:my_id>', deletecurent, name='deletecurent'),
   


]
