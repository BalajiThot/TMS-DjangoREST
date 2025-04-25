from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
    ADMIN = 'admin'
    PROJECT_MANAGER = 'project_manager'
    TECH_LEAD = 'tech_lead'
    DEVELOPER = 'developer'
    CLIENT = 'client'
    
    ROLE_CHOICES = [
        (ADMIN, 'Administrator'),
        (PROJECT_MANAGER, 'Project Manager'),
        (TECH_LEAD, 'Technical Lead'),
        (DEVELOPER, 'Developer'),
        (CLIENT, 'Client'),
    ]
    
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_name_display()

class User(AbstractUser):
    roles = models.ManyToManyField(Role, related_name='users')
    
    def __str__(self):
        return self.username