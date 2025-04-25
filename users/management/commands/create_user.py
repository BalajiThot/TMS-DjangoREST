from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Role

class Command(BaseCommand):
    help = 'Creates a new user with developer role'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username for the new user')
        parser.add_argument('password', type=str, help='Password for the new user')
        parser.add_argument('email', type=str, help='Email for the new user')

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        # Get developer role (ID 4 from previous check)
        dev_role = Role.objects.get(name='developer')
        
        user = User.objects.create_user(
            username=kwargs['username'],
            email=kwargs['email'],
            password=kwargs['password']
        )
        user.roles.add(dev_role)
        
        self.stdout.write(self.style.SUCCESS(
            f'Successfully created developer user: {user.username}'
        ))
