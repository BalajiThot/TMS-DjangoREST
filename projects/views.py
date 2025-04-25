from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from .models import Project
from .serializers import ProjectSerializer
from permissions import IsAdmin, IsProjectManager, IsTechLead, IsOwnerOrReadOnly, IsProjectMember

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        elif self.action == 'create':
            return [IsAuthenticated(), IsAdmin() or IsProjectManager()]
        else:
            return [IsAuthenticated()]
    
    def get_queryset(self):
        user = self.request.user
        
        # Admins and Project Managers can see all projects
        if user.roles.filter(name__in=['admin', 'project_manager']).exists():
            return Project.objects.all()
        
        # Others can only see projects they're members of or own
        return Project.objects.filter(Q(members=user) | Q(owner=user)).distinct()