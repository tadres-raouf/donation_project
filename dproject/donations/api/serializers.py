from rest_framework import serializers
from donations.models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'user', 'project', 'amount', 'created_at']
        read_only_fields = ['user', 'created_at']