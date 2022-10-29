# from backend.views import *
# from rest_framework.routers import DefaultRouter
# from django.urls import path,include
# router=DefaultRouter()
# router.register(r"season",SeasonModelViewSet,basename='season')
# urlpatterns=router.urls
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import season,candidate,user,round
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register(r"seasons",season.SeasonModelViewSet,basename="season")
router.register(r"candidates",candidate.CandidateModelViewSet,basename="candidate")
router.register(r"users",user.UserModelViewSet,basename="user")
router.register(r"round",round.RoundModelViewSet,basename="round")
urlpatterns=[path('login/',obtain_auth_token,name="obtain token"),]+router.urls
