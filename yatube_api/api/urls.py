from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSets, GroupViewSets, FollowViewSets, CommentViewSets

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

# dima
# dima_1234

# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NTU3NjExMSwianRpIjoiZWEwMTc5YTE3MjA2NDg2ODkwMjQxZTViODAzNDVjYTgiLCJ1c2VyX2lkIjozfQ.Fz6dUimB0yoll0PaQo7RB0MewfrHhAtiId_ZuaL8icE",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY1NTc2MTExLCJqdGkiOiI5NWMzMjcyY2ZmMjc0NjQ2YWVkNjJlNDRjN2M1ZWEyOCIsInVzZXJfaWQiOjN9.GvS_vET9eJg3hePSAHQghMBheE15_DXaAH-qZao_GQU"
# }