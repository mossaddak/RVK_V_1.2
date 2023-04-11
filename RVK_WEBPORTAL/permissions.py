from rest_framework.permissions import (
    DjangoModelPermissions,
    BasePermission,
    SAFE_METHODS
)

from rest_framework import permissions

from events.models import (
    EventRegisterUser,
    Event
)

class ReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return False
    
class IsContentEditor(permissions.BasePermission):

    def has_permission(self, request, view):

        perm = request.user.groups.filter(name='Content Editor').exists()
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser or perm:

            # print("Permissions============================", request.user.groups)
            print("Permissions============================", perm)
            return True
        
        return False
    

class IsHR(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        
        perm = request.user.groups.filter(name='Career,Event,Annoucements').exists()
        if request.method == 'POST' and request.user.is_authenticated:
            # allow normal users to POST
            return True
        
        return perm
    

class IsFinance(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.groups.filter(name='Career,Event,Annoucements').exists():
            # allow only users who belong to the 'Career,Event,Annoucements' group to POST
            return True
        
        return request.user.is_superuser


    
class RegistrationLimit(permissions.BasePermission):

    def has_permission(self, request, view):

        perm = request.user.groups.filter(name='Finance Department').exists()
        EvenRegisterUser = EventRegisterUser.objects.all()
        

        if request.method in permissions.SAFE_METHODS or request.user.is_superuser or perm:

            # print("Permissions============================", request.user.groups)
            print("Permissions============================", perm)
            return True
        
        return False
    
class AdminAccessOnlyOtherCanSee(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True  # Allow any user to create a new object

        
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user.is_superuser  # Allow only superusers to update objects
        return True 