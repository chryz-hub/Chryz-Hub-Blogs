from django.urls import path
from .views import  CreateAccount,  UpdateAccount,ShowProfilePageView, EditProfilePageView, PasswordsChangeView, CreateProfilePageView, UserDelete
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='register'),
    path('edit_profile/', UpdateAccount.as_view(), name='update_account'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='change_password'),
    path('password_success/', views.password_success, name = 'password_success'),
    path('user_delete/', UserDelete, name = 'user_delete'),
    path('profile/<username>/', ShowProfilePageView, name='show_profile_page'),
    path('edit_profile_page/<username>/', EditProfilePageView, name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='forgot_password/password_reset.html'), name='reset_password'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "forgot_password/password_reset_confirm.html"), name ='password_reset_confirm'),    
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='forgot_password/password_reset_sent.html'), name='password_reset_done'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='forgot_password/password_reset_complete.html'), name='password_reset_complete'),
]
