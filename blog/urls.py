from django.urls import path
from .views import (
    blog_list,
    create_blog,
    blog_detail,
    blog_edit,
    blog_delete
)

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('create/', create_blog, name='blog_create'),
    path('detail/<int:pk>/', blog_detail, name='blog_detail'),
    path('edit/<int:pk>/', blog_edit, name='blog_edit'),
    path('delete/<int:pk>/', blog_delete, name='blog_delete'),
]
