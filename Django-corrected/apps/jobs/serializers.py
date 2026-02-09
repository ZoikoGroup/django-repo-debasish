from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    shortDescription = serializers.CharField(source='short_description')

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'location',
            'technologies',
            'shortDescription',
            'description',
        ]

    def get_technologies(self, obj):
        return [tech.strip() for tech in obj.technologies.split(',')]
