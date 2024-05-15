from django.db import models
from django.contrib.auth.models import User
class profile(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    lid=models.CharField(max_length=10,blank=True)
    # password=models.CharField(max_length=8)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.user.username+"  ["+str(self.user.email)+"]"
# class Register(models.Model):
#     # user=models.OneToOneField(User,on_delete=models.CASCADE)
#     emailid= models.CharField(max_length=200)
#     password= models.CharField(max_length=200)
#     mobile= models.CharField(max_length=200)
#     fullname= models.CharField(max_length=200)
#     # otp=models.CharField(max_length=6)
#     # is_phone_verified=models.BooleanField(default=False)
# # def __str__(self):
# #     return self.emailid+""+self.password+""+self.mobile+""+self.fullname
# # Create your models here.
