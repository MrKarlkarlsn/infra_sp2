from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (APIGetToken, GenreViewSet, CategoryViewSet,
                       UsersViewSet, TitleViewSet, ReviewViewSet,
                       CommentViewSet, signup)

router = DefaultRouter()

router.register('titles', TitleViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', CategoryViewSet, basename='categories')
router.register('users', UsersViewSet, basename='users')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/auth/token/', APIGetToken.as_view(), name='get_token'),
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', signup),
]
