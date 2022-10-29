from rest_framework.permissions import BasePermission

class EvaluatorPermission(BasePermission):
    def has_permission(self,request,view):
        allowed=request.user.year==3 or request.user.year==4
        return allowed