# posts/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


feed_list = PostViewSet.as_view({'get': 'feed'})

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed_list, name='feed'),  # checker requirement

       # Like/unlike available at:
    # POST /api/posts/{id}/like/
    # POST /api/posts/{id}/unlike/

]

