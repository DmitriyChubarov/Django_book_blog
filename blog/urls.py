from django.urls import path

from . import views

urlpatterns = [
    path('',views.BlogListView.as_view(), name='home'),
    path('posts/<int:pk>/',views.BlogDetailView.as_view(), name='post_detail'),
    path('posts/new/',views.BlogCreateView.as_view(), name='post_new'),
    path('posts/<int:pk>/edit', views.BlogUpdateView.as_view(), name='edit_post'),
    path('posts/<int:pk>/delete', views.BlogDeleteView.as_view(), name='delete_post'),
    path('logout',views.BlogLogoutView.as_view(), name='logout_'),

]