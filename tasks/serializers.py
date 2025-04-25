from rest_framework import serializers
from .models import Task
from users.serializers import UserSerializer

class TaskSerializer(serializers.ModelSerializer):
    assigned_to_details = UserSerializer(source='assigned_to', many=True, read_only=True)
    created_by_details = UserSerializer(source='created_by', read_only=True)
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority', 
                 'created_at', 'updated_at', 'due_date', 'project',
                 'assigned_to', 'assigned_to_details', 'created_by', 'created_by_details']
        extra_kwargs = {
            'assigned_to': {'write_only': True},
            'created_by': {'write_only': True},
        }