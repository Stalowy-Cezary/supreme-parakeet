from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [
    path('', PostListView.as_view()),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create')

]