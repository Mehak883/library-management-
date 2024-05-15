from django.contrib import admin
from django.contrib import admin
from .models import AddBook,IssueBook,AddStudent,BookReturn,bookhistory
 
# Register your models here for Python Library Management System.
# from django.contrib.sessions.models import Session
# admin.site.register(Session)
class AddBook_Admin(admin.ModelAdmin):
    list_display=("bookid","bookname","author","category","status")
admin.site.register(AddBook,AddBook_Admin)
class IssueBookAdmin(admin.ModelAdmin):
    list_display=("studentuser","bookname","stuname","bookid","issuedate","expirydate","fine")
admin.site.register(IssueBook,IssueBookAdmin)
class returnbookAdmin(admin.ModelAdmin):
    list_display=("studentuser","bookname","stuname","bookid","issuedate","expirydate","fine",'returndate')
admin.site.register(BookReturn,returnbookAdmin)
class AddStudentAdmin(admin.ModelAdmin):
    list_display=("user","sname","studentid")
admin.site.register(AddStudent,AddStudentAdmin)
class bookhistoryAdmin(admin.ModelAdmin):
    list_display=("bookid",'bookname','author','category','deletedate','deletetime')
admin.site.register(bookhistory,bookhistoryAdmin)


# Register your models here.
