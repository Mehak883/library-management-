from django.urls import path
from register.views import *

urlpatterns = [
    path('regis',regis,name="regis"),
    path('login',login_att,name="login"),
    path('success',success,name="success"),
    path('already',notget,name="already"),
    path('token',token_auth,name="token"),
    path('verify/<auth_token>',verify,name="verify"),
    path('otpg',otp_page,name="otpg"),
    path('forget/<auth_token>',forget_pass,name="forget"),
    path('afterclick',afterclick,name="afterclick"),
     path('logout/',logout,name='logout'),
   

#     path('send_otp/',views.send_otp),
#     path('verify_otp/',views.verify_otp)
]
