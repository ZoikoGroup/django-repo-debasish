from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    technologies = serializers.SerializerMethodField()
    shortDescription = serializers.CharField(source='short_description')
    department_display = serializers.CharField(
        source='get_department_display',
        read_only=True
    )

    class Meta:
        model = Job
        fields = [
            'id',
            'title',
            'location',
            'technologies',
            'shortDescription',
            'description',
            'department',          # 🔥 added (raw value)
            'department_display',  # 🔥 added (readable label)
        ]

    def get_technologies(self, obj):
        return [tech.strip() for tech in obj.technologies.split(',')]
