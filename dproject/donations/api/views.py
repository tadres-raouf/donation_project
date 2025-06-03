from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from donations.models import Donation
from .serializers import DonationSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)