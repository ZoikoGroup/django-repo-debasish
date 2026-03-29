from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    plan_type_name = serializers.CharField(source='plan_type.name', read_only=True)

    class Meta:
        model = Plan
        fields = '__all__'
