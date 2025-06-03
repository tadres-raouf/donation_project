from rest_framework import serializers
from projects.models import Project, ProjectTag
from tags.models import Tag
from categories.models import Category
from accounts.models import User
from media.models import ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'name']

class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ['id', 'project', 'tag']

class ProjectSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tag.objects.all())
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'category', 'title', 'details',
            'tags', 'total_target',
            'end_time', 'is_cancelled','images'
        ]

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        request = self.context.get('request')
        user = request.user if request else None
        project = Project.objects.create(user=user, **validated_data)

        for tag in tags:
            ProjectTag.objects.create(project=project, tag=tag)
        return project

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if tags is not None:
            instance.tags.set(tags)
        return instance
      