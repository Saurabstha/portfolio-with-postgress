from . import views
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,PostDeleteView

urlpatterns = [
    # path('', views.allblogs, name='allblogs'),
    path('', PostListView.as_view(), name='allblogs'),

    # path('<int:blog_id>', views.detail, name='detailblog'),

    path('<int:pk>/', PostDetailView.as_view(), name='detailblog'),

    path('new/', PostCreateView.as_view(), name='post-create'),

    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]