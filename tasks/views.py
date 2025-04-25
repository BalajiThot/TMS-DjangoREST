from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import Task
from .serializers import TaskSerializer
from permissions import IsAdmin, IsProjectManager, IsTechLead, IsOwnerOrReadOnly, IsProjectMember

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'status', 'priority']
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdmin() or IsProjectManager() or IsTechLead() or IsOwnerOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticated(), IsAdmin() or IsProjectManager() or IsTechLead()]
        else:
            return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        
        # Admins can see all tasks
        if user.roles.filter(name='admin').exists():
            return Task.objects.all()
        
        # Project Managers can see all tasks in their projects
        if user.roles.filter(name='project_manager').exists():
            return Task.objects.filter(Q(project__owner=user) | Q(project__members=user)).distinct()
        
        # Others can only see tasks assigned to them or tasks in projects they're members of
        return Task.objects.filter(Q(assigned_to=user) | Q(created_by=user) | Q(project__members=user)).distinct()
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)