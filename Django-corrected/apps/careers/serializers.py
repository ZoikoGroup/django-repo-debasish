from rest_framework import serializers
from .models import JobApplication


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'full_name', 'email', 'phone', 'position_applied', 'resume', 'created_at']
        read_only_fields = ['id', 'created_at']