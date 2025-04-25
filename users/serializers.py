from rest_framework import serializers
from .models import User, Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)
    role_ids = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(),
        many=True,
        source='roles',
        write_only=True,
        required=False
    )
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'roles', 'role_ids', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        roles = validated_data.pop('roles', [])
        password = validated_data.pop('password')
        user = User(**validated_data)
        if(roles in ['Admin', 'Project Manager', 'Tech Lead']):
            user.is_staff = True
        else:
            user.is_staff = False
        user.role = roles
        user.set_password(password)
        user.save()
        
        if roles:
            user.roles.set(roles)
            
        return user
        
    def update(self, instance, validated_data):
        roles = validated_data.pop('roles', None)
        password = validated_data.pop('password', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        if password:
            instance.set_password(password)
            
        if roles is not None:
            instance.roles.set(roles)
            
        instance.save()
        return instance