from django.db import models
from django.contrib.auth.models import User 
from django.db.models.fields import CharField
from datetime import datetime,timedelta
# class UserExtend(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     phone = models.IntegerField()
#     def __str__(self):
#        return self.user.username
class AddBook(models.Model):
    # user = models.ForeignKey(User,default = 1, on_delete=models.CASCADE)
    bookid=CharField(max_length=10,primary_key=True)
    # bookpic=models.CharField(max_length=30 ,default=None)
    bookpic=models.ImageField(upload_to='',null=True,blank=True)
    bookname=CharField(max_length=50)
    author=CharField(max_length=20)
    category= models.CharField(max_length = 10)
    status=models.CharField(max_length=20,default='Non issued')
    def __str__(self):
        return str(self.bookname)+"["+str(self.bookid)+']   -'+str(self.status)
    
ex=datetime.now()
def expiry():
    global ex
    ex=(datetime.today() + timedelta(days=15))
    return ex


def finey():
    ds1=str()
    # s=datetime.now()-datetime.strptime(str(IssueBook.expirydate),'%B %d,%Y')
    s=datetime.today()-IssueBook.expiree
    for i in str(s):
        if(i!=" "):
            ds1=ds1+i
        else:
            break
    days=int(ds1)
    if(days>0):
        f=days*4
    else:
        f=0
    return f    

class IssueBook(models.Model):
  
    studentuser=models.CharField(max_length=100, blank=True) 
    bookname=models.CharField(max_length=20,blank=True)
    stuname=models.CharField(max_length=20,blank=True)
    bookid=models.CharField(max_length=20)
    # bookpic=models.ImageField(upload_to='',null=True,blank=True)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=expiry)
    fine=models.IntegerField(default=0)
    def expiree(self):
        self.ex=ex
        return self.ex


class BookReturn(models.Model):
    studentuser=models.CharField(max_length=100, blank=True) 
    bookname=models.CharField(max_length=20,blank=True)
    stuname=models.CharField(max_length=20,blank=True)
    bookid=models.CharField(max_length=20)
    issuedate=models.DateField()
    expirydate=models.DateField()
    fine=models.IntegerField()
    returndate=models.DateField(auto_now=True)



class bookhistory(models.Model):
    bookid=CharField(max_length=10,primary_key=True)
    bookname=CharField(max_length=50)
    author=CharField(max_length=20)
    category= models.CharField(max_length = 10)
    deletedate=models.DateField(auto_now=True)
    deletetime=models.TimeField(auto_now=True)



class AddStudent(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    sname=models.CharField(max_length=30)
    studentid=models.CharField(max_length=20)
    def __str__(self):
        return self.sname+'['+str(self.studentid)+']'