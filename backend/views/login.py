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
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

CLIENT_ID=config('CLIENT_ID')
CLIENT_SECRET=config('CLIENT_SECRET')

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def initial_login(request):
    url=f'https://channeli.in/oauth/authorise/?client_id={CLIENT_ID}&redirect_uri=http://127.0.0.1:1000/get_oauth_token/'
    return redirect(url)


def GetOrCreateUser(user_id,username,name,enrolment,year,branch,dob,email_id,phone):
    # user=User.objects.create_user(user_id,username,name,enrolment,branch,year,email_id,phone,dob)
    print("created")
    print(user_id)
    try:
        user=User.objects.get(username=username)
        return user
    except :
        print('hello')
        user=User.objects.create(UserId=user_id,username=username,name=name,EnrollmentNo=enrolment,branch=branch,year=year,EmailId=email_id,phone=phone,dob=dob)
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
        "redirect_uri":"http://127.0.0.1:1000/get_oauth_token/",
        "code":request.GET.get('code',None),
    }
    
    response=requests.post('https://channeli.in/open_auth/token/',data)
    print('done')
    print(response.status_code)
    data=response.json()
    print(data)
    ACCESS_TOKEN=data['access_token']
    REFRESH_TOKEN=data['refresh_token']
    TOKEN_TYPE=data['token_type']
    print(ACCESS_TOKEN)
    print(REFRESH_TOKEN)
    print(TOKEN_TYPE)    
    header={
        "Authorization":"Bearer "+ACCESS_TOKEN
    }
    print(header)
    values=requests.get('https://channeli.in/open_auth/get_user_data/',headers=header)
        
    value_dict=values.json()
    print(value_dict)

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

    for role in value_dict['person']['roles']:
        if (role['role']=="Maintainer"):
            status=True

    if status==True:
        print('entered')
        try:
            user=GetOrCreateUser(user_id=user_id,username=username,name=name,branch=branch,year=year,dob=dob,email_id=email_id,phone=phone,enrolment=enrolment)
        except:
            return Response("User failed to create")
        try:
            login(request,user,backend=None)
        except:
            return Response("Login failed")
    else:
        return Response("not an Img member")
    return redirect("http://127.0.0.1:1000/")

    @api_view([])
    def logout_view(request):
        if request.user.is_authenticated:
            logout(request)


    

