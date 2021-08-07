from django.urls import path
from .views import BlogList, BlogDetail, LoginToBlog, CreateBlog, EditBlog, DeleteBlog, AddCategory, CategoryView, CategoryList, LikeView, SearchResultsView, DeleteComment
from . import views

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
    path('create_blog/', CreateBlog.as_view(), name='create_blog'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('login_blog/', LoginToBlog.as_view(), name='login_blog'),
    path('edit_blog/<int:pk>/', EditBlog.as_view(), name='edit_blog'),
    path('delete_blog/<int:pk>/', DeleteBlog.as_view(), name='delete_blog'),
    path('category/<str:category>', CategoryView, name='category'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('blogcategory/<str:category>', CategoryView, name='blogcategory'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('delete_comment/<int:pk>/', DeleteComment.as_view(), name ='delete_comment'),
]
