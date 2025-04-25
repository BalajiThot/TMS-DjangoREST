from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import Comment
from .serializers import CommentSerializer
from permissions import IsOwnerOrReadOnly

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        else:
            return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        
        # Admins can see all comments
        if user.roles.filter(name='admin').exists():
            return Comment.objects.all()
        
        # Filter comments based on projects and tasks the user has access to
        return Comment.objects.filter(
            models.Q(project__members=user) |
            models.Q(task__assigned_to=user) |
            models.Q(task__project__members=user) |
            models.Q(author=user)
        ).distinct()
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)