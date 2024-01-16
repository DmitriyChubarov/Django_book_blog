from django.urls import path

from . import views

urlpatterns = [
    path('',views.BlogListView.as_view(), name='home'),
    path('posts/<int:pk>/',views.BlogDetailView.as_view(), name='post_detail'),
    path('posts/new/',views.BlogCreateView.as_view(), name='post_new'),
]