from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import redirect
from decouple import config
from rest_framework.views import APIView
from django.contrib.auth import login, authenticate, logout
# from backend.models import User
import requests
from rest_framework import request
from rest_framework import status
from urllib.request import Request
# from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
User=get_user_model()

CLIENT_ID=config('CLIENT_ID')
CLIENT_SECRET=config('CLIENT_SECRET')


def get_username(username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("http://127.0.0.1:8000/")

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def initial_login(request):
    url=f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri=http://127.0.0.1:8000/get_oauth_token/'
    return redirect(url)


def GetOrCreateUser(user_id,username,name,enrolment,year,branch,dob,email_id,phone):
    # user=User.objects.create_user(user_id,username,name,enrolment,branch,year,email_id,phone,dob)
    try:
        user=User.objects.get(username=username)
        print(user)
        return user
    except User.DoesNotExist :
        # print('hello')
        user=User.objects.create(UserId=user_id,username=username,name=name,EnrollmentNo=enrolment,branch=branch,year=year,EmailId=email_id,phone=phone,dob=dob)
        user.save()
        return user
        # user=User.objects.get(username=username)

@api_view(['GET','POST'])
@authentication_classes([])
@permission_classes([])
def GetToken(request):
    
    print(request.GET.get('code',''))
    data={
        'client_id':CLIENT_ID,
        'client_secret':CLIENT_SECRET,
        "grant_type":"authorization_code",
        "redirect_uri":"http://127.0.0.1:8000/get_oauth_token/",
        "code":request.GET.get('code',None),
    }
    
    response=requests.post('https://channeli.in/open_auth/token/',data)
    # print('done')
    # print(response.status_code)
    data=response.json()
    # print(data)
    ACCESS_TOKEN=data['access_token']
    REFRESH_TOKEN=data['refresh_token']
    TOKEN_TYPE=data['token_type']  
    header={
        "Authorization":"Bearer "+ACCESS_TOKEN
    }
    print(header)
    values=requests.get('https://channeli.in/open_auth/get_user_data/',headers=header)
        
    value_dict=values.json()
    # print(value_dict)

    name=value_dict['person']['fullName']
    username=value_dict['username']
    user_id=value_dict['userId']
    enrolment=value_dict['student']['enrolmentNumber']
    year=value_dict['student']['currentYear']
    branch=value_dict['student']['branch department name']
    dob=value_dict['biologicalInformation']['dateOfBirth']
    email_id=value_dict['contactInformation']['instituteWebmailAddress']
    phone=value_dict['contactInformation']['primaryPhoneNumber']
    status=False

    print(type(name),type(username),type(user_id),type(enrolment),type(year),type(branch),type(dob),type(email_id),type(phone))
    for role in value_dict['person']['roles']:
        if (role['role']=="Maintainer"):
            status=True

    if status==True:
        try:
            # print('entered')
            user=GetOrCreateUser(user_id=user_id,username=username,name=name,branch=branch,year=year,dob=dob,email_id=email_id,phone=phone,enrolment=enrolment)
        except:
            return Response("User failed to create")
        try:
            login(request,user,backend=None)
            return Response("LoggedIn")
        except:
            return Response("Login failed")
    else:
        return Response("not an Img member")
    return redirect("http://127.0.0.1:8000/")

   

    

    

