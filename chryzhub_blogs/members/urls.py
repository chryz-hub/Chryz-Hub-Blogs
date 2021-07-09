from django.urls import path
from .views import  CreateAccount,  UpdateAccount, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='register'),
    path('edit_profile/', UpdateAccount.as_view(), name='update_account'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='change_passowrd'),
    path('password_success', views.password_success, name = 'password_success'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
