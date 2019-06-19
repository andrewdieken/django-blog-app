from django.urls import path
from .views import BlogDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    # all blog post entries will now start with post/ attached to the end will be the primary key
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]
