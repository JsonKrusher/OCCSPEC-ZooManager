from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('register/', views.register_page, name='register_page'),
    path('logout/', views.logout_function, name='logout'),
    path('change-password/', views.change_password_function, name='change_password_page'),
]
