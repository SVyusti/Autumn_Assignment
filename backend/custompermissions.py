from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
user=get_user_model()
class EvaluatorPermission(BasePermission):
    def has_permission(self,request,view):
        allowed=request.user.year==3 or request.user.year==4
        return allowed

# from rest_framework.authentication import BaseAuthentication
# from django.contrib.auth.models import User
# from rest_framework.exceptions import AuthenticationFailed

# class CustomAuthentication(BaseAuthentication):
#     def authenticate(self,request):
#         username=request.GET.get('username')
#         if username is None:
#             return None

#         try:
#             user=User.objects.get(username=username)
#         except User.DoesNotExist:
#             raise AuthenticationFailed('No Such User')
#         return (user,None)