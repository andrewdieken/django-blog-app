from django.urls import path
from .views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdateView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    # all blog post entries will now start with post/ attached to the end will be the primary key
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete')
]
