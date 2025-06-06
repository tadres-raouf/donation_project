from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register('', CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]