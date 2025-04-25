from rest_framework import serializers
from .models import Project
from users.serializers import UserSerializer

class ProjectSerializer(serializers.ModelSerializer):
    owner_details = UserSerializer(source='owner', read_only=True)
    member_details = UserSerializer(source='members', many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 
                 'owner', 'owner_details', 'members', 'member_details']
        extra_kwargs = {
            'owner': {'write_only': True},
            'members': {'write_only': True},
        }