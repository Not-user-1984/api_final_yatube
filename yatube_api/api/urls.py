from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CommentViewSets,
    FollowViewSets,
    GroupViewSets,
    PostViewSets
)

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSets)
v1_router.register('groups', GroupViewSets)
v1_router.register('follow', FollowViewSets, basename='follow')
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSets,
    basename='comments'

)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comments_id>\d+)',
    CommentViewSets,
    basename='comments_detail'
)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
