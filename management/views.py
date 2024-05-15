from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime,timedelta,date
from .models import IssueBook,AddBook,BookReturn,AddStudent,bookhistory
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login
from django.contrib.auth.decorators import login_required
from register.models import profile
from management.forms import IssueBookForm
import datetime 
@login_required
def home(request):
    return render(request,'home.html') 
@login_required
def hom1(request):
    return render(request,'hom1.html') 
# Create your views here.
@login_required
def view_books(request):
    books = AddBook.objects.all().order_by('bookid')
    messages.success(request,'All Books')
    return render(request,'view_books.html',{'book':books})    

# def addbook(request):
#     Book = AddBook.objects.all()
#     return render(request,'addbook.html',{'Book':Book})
@login_required
def search_book(request):
    if request.method=="POST":
        bookname=request.POST["bookname"]
        book=AddBook.objects.filter(bookname__contains=bookname)
        messages.success(request,'you searched for')
        return render(request,'view_books.html',{'book':book})
    else:
        messages.success(request,'book not found')
        return render(request,'view_books.html')

@login_required
def edit_book(request,id):
    editbook=AddBook.objects.filter(bookid=id).values()
    if request.method=="POST":
        e=AddBook()
        e.bookid=editbook[0]['bookid']
        e.bookpic=editbook[0]['bookpic']
        e.bookname=request.POST["bookname"]
        e.author=request.POST["authorname"]
        e.category=request.POST["category"]
        e.status=editbook[0]['status']
        e.save()
        messages.success(request,'book record is updated ')
        return redirect('/viewbook')
    return render(request,'editbook.html',{'editbook':editbook})




@login_required
def deletebook(request,id):
    # if request.session.has_key('is_logged'):
    try:
        AddBook_info = AddBook.objects.get(bookid=id)
        if IssueBook.objects.filter(bookid=id).first():
            messages.success(request,"book is issued to a student, not able to delete")
            return redirect("/viewbook")
        deletebk=bookhistory(bookid=AddBook_info.bookid,bookname=AddBook_info.bookname,author=AddBook_info.author,category=AddBook_info.category)
        AddBook_info.delete()
        deletebk.save()
        return redirect("/viewbook")

    except Exception as e:
         print(e)
    return render(request,"view_book.html") 


def book_history(request):

    books = bookhistory.objects.all().order_by('bookid')
    messages.success(request,'All Deleted Books')
    return render(request,'book_history.html',{'book':books})    

@login_required
def search_book_history(request):
    if request.method=="POST":
        bookname=request.POST["bookname"]
        if bookhistory.objects.filter(bookname__contains=bookname):
            book=bookhistory.objects.filter(bookname__contains=bookname)
            messages.success(request,f'you searched for {bookname}')
            return render(request,'book_history.html',{'book':book})
        else:
            messages.success(request,'book not found')
            return redirect('/bookhistory')
    else:
        messages.success(request,'book not found')
        return redirect('/bookhistory')
    return render(request,'book_histroy.html')

@login_required
def AddBookSubmission(request):
    # if request.session.has_key('is_logged'):
        if request.method == "POST":
            # user_id = request.session["user_id"]
            # user1 = User.objects.get(id=user_id)
            bookid = request.POST.get('bookid')
            bookname = request.POST.get('bookname')
            authorname = request.POST.get('authorname')
            category=request.POST.get('category')
            coverpage=request.FILES.get('coverpage')
            print(coverpage)
            cbook_id=AddBook.objects.filter(bookid=bookid).first()
            if cbook_id:
                 messages.success(request,'book is also recorded ')
                 return redirect('/addbook')
            add = AddBook.objects.create(bookid=bookid,bookpic=coverpage,bookname=bookname,author=authorname,category=category)
            add.save()
            messages.success(request,'book is saved')
            return redirect ('/addbook')
            # Book = AddBook.objects.all()
        # return redirect('/')
        # return HttpResponse("hi everyone")
        return render(request,'add_book.html')

@login_required
def students(request):
    student = profile.objects.all()
    messages.success(request,'All students')
    return render(request,'view_subscribers.html',{'student':student})




@login_required
def search_student(request):
    if request.method=="POST":
        username=request.POST["username"]
        user1=User.objects.filter(username__contains=username)
        l=list()
        for e in user1:
            stu=profile.objects.filter(user=e)
            l.append(stu)
        messages.success(request,f'you searched for {username}')
        print(l)
        print("hlooo\n\n")
        return render(request,'view_subscribers.html',{'l':l})
    else:
        messages.success(request,f'searched for {username} failed')
        return render(request,'view_subscribers.html')




@login_required
def issue_book(request):
    form=IssueBookForm()
    if request.method=='POST':
        form=IssueBookForm(request.POST)
        if form.is_valid():
            name2=request.POST['name2']
            id2=request.POST['id2']
            # to filter username of the given id 
            # name2 = form.cleaned_data.get("name2")
            u1= User.objects.filter(email=name2).first()
            p= profile.objects.filter(user=u1).first()
            if p:
                if p.lid:
                    messages.success(request,'Book can not be issued to liberarian')
                    return redirect('/issue_book')
                if IssueBook.objects.filter(bookid=id2).first():
                    messages.success(request,'Book Already Issued')
                    return redirect('/issue_book')
                else:
                    print('hloo\n\n')
                # if profile.objects.filter(id=name2).first():
                    bookn_obj=AddBook.objects.filter(bookid=id2).first()
                    bookn=str(bookn_obj.bookname)
                    bookn_obj.status='Issued'
                    bookn_obj.save()
                    name_obj=User.objects.filter(email=name2).first()
                    studn=str(name_obj.username)

                    obj=IssueBook.objects.create(studentuser=name2,bookname=bookn,stuname=studn,bookid=id2)
                    obj.save()
                    messages.success(request,'Book Issued To Students Successfully')
                    redirect('/')
            else:
                    messages.success(request,'Book can not be issued to admin')
                    return redirect('/issue_book')
                # else :
                #     print('problem\n\n')
    return render(request,'issuebook.html',{'form':form})




@login_required
def student_issued_books(request):
    print(request.user.username)
    issuedBooks = IssueBook.objects.filter(stuname=request.user.username)
    print(issuedBooks)
    details = []
    messages.success(request,'All Issued Books')
    for i in issuedBooks:
        fine=finey(i.expirydate)       
        # books = list(AddBook.objects.filter(bookid=i.bookid))
        # print(books)
        t=(i.bookname,i.bookid,i.issuedate,i.expirydate,fine)
        details.append(t)
    return render(request,'view_issued_book_stud.html',{'details':details,})



@login_required
def search_issue(request):
    if request.method=="POST":
        stuname=request.POST["stuname"]
        book=IssueBook.objects.filter(stuname__contains=stuname)
        detail=[]
        for i in book:
            f=finey(i.expirydate)
            t=(i.stuname ,i.bookname,i.bookid,i.issuedate,i.expirydate,f)
            detail.append(list(t))
        messages.success(request,f'you searched for {stuname}')
        return render(request,'view_issued_book.html',{'detail':detail})
    else:
        messages.success(request,'book not found')
        return redirect('/view_issued_books')
    
    return render(request,'view_issued_books.html')
    


@login_required
def view_issued_books(request):
    books = list(IssueBook.objects.all())
    detail=[]
    for i in books:
        print(type(i.expirydate))
        f=finey(i.expirydate)
        t=(i.stuname ,i.bookname,i.bookid,i.issuedate,i.expirydate,f)
        detail.append(list(t))

    messages.success(request,'All Issued Books')
    return render(request,'view_issued_book.html',{'detail':detail})        

def finey(expiree):
    print("hooo",type(expiree))
    s=date.today()-expiree
    ds1=""
    for i in str(s):
        if(i!=" "):
            ds1=ds1+i
        else:
            break
    print(ds1)
    days=int(ds1)
    if(days>0):
        f=days*4
    else:
        f=0
    return f    



@login_required
def view_books_stud(request):
    books = AddBook.objects.all().order_by('bookname')
    messages.success(request,'All Issued Books') 
    return render(request,'view_books_stud.html',{'book':books})   





@login_required
def searchbookstud(request):
    if request.method=="POST":
        bookname=request.POST["bookname"]
        book=AddBook.objects.filter(bookname__contains=bookname)
        messages.success(request,f'you searched for {bookname}')
        return render(request,'view_books_stud.html',{'book':book})
    else:
        messages.success(request,'book not found')
        return redirect('/view_books_stud')
    return render(request,'view_books_stud.html')





@login_required
def students_delete(request, id):
    # print('\n',id)
    try:
        subscriber = profile.objects.get(id=id)
        em =subscriber.user.email
        if IssueBook.objects.filter(studentuser=em).first():
            messages.success(request,"book is issued to that student ,can't delete record")
            return redirect('/students')
        User_p=User.objects.get(email=em)
        subscriber.delete()
        User_p.delete()

        return redirect("/students")
    except Exception as e:
         print(e)
    return render (request,'view_subscribers.html')



@login_required
def ReturnBook(request,id):
    try:
        rb=IssueBook.objects.get(bookid=id)
        fine=finey(rb.expirydate)
        br=BookReturn(studentuser=rb.studentuser,bookname=rb.bookname,stuname=rb.stuname,bookid=rb.bookid,issuedate=rb.issuedate,expirydate=rb.expirydate,fine=fine)
        rb.delete()
        br.save()
        statusaddbook=AddBook.objects.filter(bookid=id).first()
        statusaddbook.status="Non issued"
        statusaddbook.save()                                                                                                                                                                                
        messages.success(request,'book returned')
        return redirect("/view_issued_books")
    except Exception as e:
        print(e)
    return render(request,'view_issued_book.html')

@login_required
def issue_history(request):
    books = BookReturn.objects.all().order_by('stuname')
    messages.success(request,'All Returned Books')
    return render(request,'view_issued_history.html',{'book':books})    



@login_required
def search_issue_history(request):
    if request.method=="POST":
        stuname=request.POST["stuname"]
        book=BookReturn.objects.filter(stuname__contains=stuname)
        messages.success(request,f'you searched for {stuname}')
        return render(request,'view_issued_history.html',{'book':book})
    else:
        messages.success(request,'book not found')
        return redirect('/returnbook-history')
    return render(request,'view_issued_history.html')
