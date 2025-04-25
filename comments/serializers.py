from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author_details = UserSerializer(source='author', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'updated_at', 
                 'author', 'author_details', 'project', 'task']
        extra_kwargs = {
            'author': {'write_only': True},
        }