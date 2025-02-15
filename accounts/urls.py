from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name='account'),
    path('account/edit/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
] 