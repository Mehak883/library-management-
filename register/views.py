from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as lmn
from django.contrib.auth.decorators import login_required
from django.template import loader
import requests
from django.contrib import messages
# from .helpers import send_otp_to_phone_number
from .models import profile
import random
import http.client
from django.conf import settings
from django.core.mail import send_mail
import uuid
# from register.form import regform
l=[]

def regis(request):
    if request.method =='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        lid=request.POST.get('lid')
        passw=request.POST.get('password')
        check_user=User.objects.filter(email=email).first()
        try:
            if len(str(passw))>8:
                messages.success(request,'password length is more than 8 characters')
                return redirect('/regis')
            if check_user:
                messages.success(request,'User Already Exist')
                return redirect('/regis')
            else:
                user=User(email=email,username=name)
                user.set_password(passw)
                user.save()
                auth_token=str(uuid.uuid4())
                if (lid=="2023lms"):
                    prof=profile.objects.create(user=user,lid=lid,auth_token=auth_token)
                    prof.save()
                else:
                    prof=profile.objects.create(user=user,auth_token=auth_token)
                    prof.save()
                send_mail_aftr_regis(name,email,auth_token)
                messages.success(request,'Mail has been send to you,Kindly check your email')
                return redirect('/regis')
        except Exception as e:
            print(e)    
    return render(request,'reg1.html')



def login_att(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(password)
        user_obj=User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request,'user not found')
            return redirect('/login')
        else:
            profile_obj=profile.objects.filter(user=user_obj).first()
            if not profile_obj.is_verified:
                messages.success(request,'user not found')
                return redirect('/login')
            user=authenticate(username=username,password=password)
            if user is None:
                messages.success(request,'wrong password')
                return redirect('/login')
            login(request,user)
            if profile_obj.lid:
                messages.success(request,'logged in')
                return redirect('/home')
            else:
                return redirect('/hom1')
    return render(request,'login.html')




def success(request): 
    return render(request,'success.html')



def notget(request):
    return render(request,'notget.html')



def token_auth(request):
    return render(request,'token_send.html')



def send_mail_aftr_regis(name,email,token):
    subject="Your account need to be verified"
    message=f'welcome {name}\nkindly click on the link to verify your email http://127.0.0.1:8000/verify/{token}'
    email_from =settings.EMAIL_HOST_USER
    recipient_list=[email] 
    send_mail(subject,message,email_from,recipient_list)




def send_mail_frgt_pass(name,email,token):
    subject="Change password"
    message=f'welcome {name}\nkindly click on the link to create new password http://127.0.0.1:8000/forget/{token}'
    email_from =settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)




def forget_pass(request,auth_token):
    global l
    if request.method =='POST':
        passw=request.POST.get('password')
        c_pass=request.POST.get('c_pass')
        if(passw==c_pass):
            user=User.objects.get(email=l[0])
            user.set_password(passw)
            user.save()
            l=[]
            messages.success(request,'password changes succesfully')
            return redirect('/success')

    return render(request,'pass.html')


def afterclick(request):
    if request.method =='POST':
        email=request.POST.get('email')
        name=request.POST.get('name')
        check_user=User.objects.filter(email=email).first()
        check_user=User.objects.filter(username=name).first()
        try:
                print('hi')
                if check_user is None :

                    messages.success(request,'User not Exist')
                    return redirect('/afterclick')     
                auth_token=str(uuid.uuid4())
                print("hlo")
                # prof=profile.objects.create(user=user,mobile=mobile,auth_token=auth_token)
                l.append(email)

                send_mail_frgt_pass(name,email,auth_token)
                print('after snd')
                messages.success('mail has been sent to you,Kindly check your mailbox')
                return redirect('/afterclick')
        except Exception as e:
                print("hloooo",e)    
    return render(request,'forgetpassnextpage.html')




def verify(request,auth_token):
    try:
        profile_obj=profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                 messages.success(request,'your account has been already verified')
                 return redirect('/home')
            profile_obj.is_verified=True
            profile_obj.save()
            messages.success(request,'your account has been verified')
      
            # messages.success(request,'Your account has been verified')
            if profile_obj.lid:
                return redirect('/home')
            else:
                return redirect('/hom1')
        else:
            q1={'msg':"wrong email please check it"}
            # messages.success(request,'Your account has been verified')
            return render(request,'/already')
    except Exception as e:
        print(e)
    

@login_required
def otp_page(request):
    return render(request,'otp.html')


def logout(request):
    lmn(request)
    messages.success(request,'Log out Sucessfully')
    return redirect('/login')
# def send_otp(mobile,otp):
#     conn=http.client.HTTPSConnection("api.msg91.com")
#     authkey=settings.authkey
#     headers={'content-type':"application/json"}
#     url="http://control.msg91.com/api/sendotp.php?otp="+otp+'&sender=abc&message='+'your otp is '+otp+"&mobile="+mobile+"&authkey="+authkey+"&country=91"
# def regis(request):
    # regi=regform()
    # return render(request,"reg1.html",{})
# @api_view(['POST'])
# def send_otp(request):
#      data=request.data

#      if data.get('mobile') is None:
#          return Response({
#               'status':400,
#               'message':'key phone_number is required'
#         })
#      if data.get('password') is None:
#         return Response({
#             'status':400,
#            'message':'key password is required'
#          })
#      user=Register.objects.create(phone_number=data.get('mobile'),
#     otp=send_otp_to_phone_number(data.get('mobile'))
#     )
#     user.set_password=data.get('set_password')
#     user.save()
#     return Response({
#         'status':200,'message': 'Otp sent'
#     })

# url = "https://control.msg91.com/api/v5/otp?mobile=&template_id="

# payload = {
#     "Param1": "value1",
#     "Param2": "value2",
#     "Param3": "value3"
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "authkey": "Enter your MSG91 authkey"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.text)  

# @api_view(['POST'])
# def verify_otp(request):
#     data=request.data

#     if data.get('mobile') is None:
#         return Response({
#             'status':400,
#             'message':'key phone_number is required'
#         })
#     if data.get('otp') is None:
#         return Response({
#             'status':400,
#             'message':'key otp is required'
#         })
#     try:
#         user_obj = Register.objects.get(mobile=data.get('mobile'))
#     except Exception as e:
#         return Response({
#             'status':400,
#             'message':'invalid phone'
#         })
#     if user_obj.otp==data.get('otp'):
#         user_obj.is_phone_verified=True
#         user_obj.save()
#         return Response({
#             'status':200,
#             'message':'otp matched'
#         })
#     return Response({
#         'status' : 400,
#         'message':'invalid otp'
#     })
