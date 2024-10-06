
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.HomePage.as_view(),name='home'),
    path('add/',views.AddTask.as_view(),name='add'),
    path('update/<int:pk>',views.updateTask.as_view(),name='update'),
    path('delete/<int:pk>',views.DeletePage,name='delete'),
    path('login/',views.LoginPage.as_view(),name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('signup/',views.Signuppage.as_view(),name='signup'),
    path('done/<int:pk>',views.DonePage,name='done'),
    


]