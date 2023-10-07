from django.urls import path
from .views import (
    BlogListView,
    BlogDeteView,
    BlogCreateView,
    BlogUbdateView,
    BlogDeleteView,
    My_view,
)

urlpatterns = [
    # path('post/<int:pk>/delete/', My_view.as_view(), name='delete'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', BlogUbdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDeteView.as_view(), name='post_detail'),
]