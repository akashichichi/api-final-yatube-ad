from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='v1_posts')
router.register(r'groups', GroupViewSet, basename='v1_groups')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='v1_comments')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
