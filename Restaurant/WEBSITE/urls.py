from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('reservations/', views.reservation, name='reservations'),
    path('about/', views.about, name='about'),
    path('profile/', views.user_profile, name='profile'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/<int:pk>', views.delete_user, name='delete_user'),
    path('delete_reserve/<str:pk>', views.delete_reserve, name='delete_reserve'),
    path('contact-us/', views.contact, name='contactpage'),
]
