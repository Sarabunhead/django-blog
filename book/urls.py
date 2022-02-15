from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView



urlpatterns = [
    # path("",views.post_list,name="post_list"),
    path('',HomeView.as_view(), name="list"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name = "article-ditail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
]
