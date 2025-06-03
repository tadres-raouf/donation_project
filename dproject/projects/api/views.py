from rest_framework import viewsets
from projects.models import Project, ProjectTag
from .serializers import ProjectSerializer, ProjectTagSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from tags.models import Tag

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def similar(self, request, pk=None):
        project = self.get_object()
        tags = project.tags.values_list('id', flat=True)
        similar_projects = Project.objects.filter(tags__in=tags).exclude(id=project.id).distinct()[:4]
        serializer = self.get_serializer(similar_projects, many=True)
        return Response(serializer.data)

class ProjectTagViewSet(viewsets.ModelViewSet):
    queryset = ProjectTag.objects.all()
    serializer_class = ProjectTagSerializer