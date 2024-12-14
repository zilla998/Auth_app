from django.urls import path
from . import views

urlpatterns = [
    # Регистрация и аутентификация
    path('singup/', views.SingUpView.as_view(), name='singup')
]