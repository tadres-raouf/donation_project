from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'project', 'content', 'create_at', 'update_at']
        read_only_fields = ['user', 'create_at', 'update_at']