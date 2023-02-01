from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.handleSignUp,name='handleSignUp'),
    path('login',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('contact/',views.handlecontact,name='handlecontact'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('mail/',views.handlemail,name='mail'),
    path('pdf/',views.pdf,name='pdf'),
    
]