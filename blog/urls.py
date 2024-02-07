from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home, name="blog_home"),
    path('create/post/', views.createPost, name="create_post"),
    path('post/like/', views.like, name="like_post"),
    path('categories/', views.categories, name="category"),
    path('post/dislike/', views.dislike, name="dislike_post"),
    path('post/category/<str:category>/', views.categoryPost, name="category_post"),
    path('post/category/<str:category>/<str:username>', views.categoryPost, name="category_post_user"),
    path('post/user/<str:username>/', views.userPost, name="user_post"),
    path('post/delete/', views.delete, name="delete_post"),
    path('post/<slug:slug>/', views.post, name="post_detail"),
    path('post/<slug:slug>/update/', views.update, name="update_post"),
    path('post/<slug:slug>/post-comment/', views.postComment, name="post_comment"),
    path('post/<slug:slug>/<int:id>/delete-comment/', views.deleteComment, name="delete_comment"),
]   