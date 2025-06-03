from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import ProjectViewSet, ProjectTagViewSet

router = DefaultRouter()
router.register('', ProjectViewSet, basename='projects')
router.register(r'tags', ProjectTagViewSet, basename='project-tags')

urlpatterns = [
    path('', include(router.urls)),
]