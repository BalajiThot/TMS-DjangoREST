from django.contrib import admin

# Register your models here.
class IsAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj = None):
        return request.user.is_superuser or getattr( request.user, 'role', None) in ['Admin', 'Project Manager', 'Tech Lead', 'Developer', 'Client']
    

    
