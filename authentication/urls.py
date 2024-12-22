from django.urls import path
from authentication import views


urlpatterns = [
    path('register/', views.user_registration, name='register'),
    path('login/', views.user_login, name='login')
]