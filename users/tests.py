from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Role

class UserAPITests(TestCase):
    def setUp(self):
        # Create roles
        self.admin_role = Role.objects.create(name=Role.ADMIN)
        self.pm_role = Role.objects.create(name=Role.PROJECT_MANAGER)
        
        # Create admin user
        self.admin_user = User.objects.create_user(
            username='admin', email='admin@example.com', password='password'
        )
        self.admin_user.roles.add(self.admin_role)
        
        # Create regular user
        self.user = User.objects.create_user(
            username='testuser', email='test@example.com', password='password'
        )
        self.user.roles.add(self.pm_role)
        
        self.client = APIClient()
    
    def test_register_user(self):
        url = reverse('user-list')
        data = {
            'username': 'newuser',
            'email': 'new@example.com',
            'password': 'password',
            'first_name': 'New',
            'last_name': 'User',
            'role_ids': [self.pm_role.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 3)
        
    def test_login_user(self):
        url = reverse('user-login')
        data = {
            'username': 'testuser',
            'password': 'password'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        
    def test_update_user(self):
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        url = reverse('user-detail', args=[self.user.id])
        data = {
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Refresh user from database
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Updated')