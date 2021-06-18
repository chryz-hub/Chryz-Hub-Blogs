from django.urls import path
from .views import BlogList, BlogDetail, CreateBlog, EditBlog, DeleteBlog, CreateAccount, LoginToBlog, AddCategory, CategoryView, CategoryList, LikeView, UpdateAccount, PasswordsChangeView
#from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', CreateAccount.as_view(), name='register'),
    path('edit_profile/', UpdateAccount.as_view(), name='update_account'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='change_passowrd'),
    path('password_success', views.password_success, name = 'password_success'),
    path('', BlogList.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('create_blog/', CreateBlog.as_view(), name='create_blog'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('edit_blog/<int:pk>/', EditBlog.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>/', DeleteBlog.as_view(), name='delete_blog'),
    path('login_blog/', LoginToBlog.as_view(), name='login_blog'),
    path('category/<str:category>', CategoryView, name='category'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('blogcategory/<str:category>', CategoryView, name='blogcategory'),
    path('like/<int:pk>>', LikeView, name='like_post'),
    ]
