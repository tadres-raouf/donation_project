
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ratings.models import Rating
from .serializers import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Rating.objects.all()

    def perform_create(self, serializer):
        
        project = serializer.validated_data['project']
        existing_rating = Rating.objects.filter(user=self.request.user, project=project).first()
        if existing_rating:
            existing_rating.value = serializer.validated_data['value']
            existing_rating.save()
        else:
            serializer.save(user=self.request.user)