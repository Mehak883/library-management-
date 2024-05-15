from django.urls import path
from management import views

urlpatterns = [
    path('home',views.home,name="home"),


    path('hom1',views.hom1,name="hom1"),
    # path('',views.index,name='index'),
    # path('staff/',views.staff,name='staff'),
    # path('stafflogin/',views.stafflogin,name='stafflogin'),
    # path('staffsignup/',views.staffsignup,name='staffsignup'),
    # path('dashboard/',views.dashboard,name='dashboard'),
    # path('addbook/',views.addbook,name='addbook'),
    # path('SignupBackend/',views.SignupBackend,name='SignupBackend'),
    # path('LoginBackend/',views.LoginBackend,name='LoginBackend'),
    path('addbook',views.AddBookSubmission,name='addbook'),
    path('viewbook',views.view_books,name='viewbook'),
    path('searchbook',views.search_book,name='searchbook'),
    path('editbook/<int:id>',views.edit_book,name='editbook'),
    path('view_books_stud',views.view_books_stud,name='view_books_stud'),
    path('searchbookstud',views.searchbookstud,name='searchbookstud'),
    path('deletebook/<int:id>',views.deletebook,name='deletebook'),
    path('bookhistory',views.book_history,name='bookhistory'),
    path('search-book-history',views.search_book_history,name='search-book-history'),
    path('students',views.students,name='students'),
    path('searchstudent',views.search_student,name='searchstudent'),
    path('students_delete/<int:id>',views.students_delete,name='students_delete'),
    path('issue_book/',views.issue_book,name='issue_book'),
    path('searchissue/',views.search_issue,name='searchissue'),
    path('view_issued_books',views.view_issued_books,name='view_issued_books'),
    path('ReturnBook/<int:id>',views.ReturnBook,name='ReturnBook'),
    path('returnbook-history',views.issue_history,name='returnbook-history'),
    path('student_issued_books',views.student_issued_books,name='student_issued_books'),
    path('search-returnbook-history',views.search_issue_history,name='search-returnbook-history'),
   
    # path('returnbook/',views.returnbook,name='returnbook'),
    # path('HandleLogout/',views.HandleLogout,name='HandleLogout'),
    # path('issuebooksubmission/',views.issuebooksubmission,name='issuebooksubmission'),
    # path('returnbooksubmission/',views.returnbooksubmission,name='returnbooksubmission'),
    # path('Search/',views.Search,name='Search'),
    # path('Searchstudent/',views.Searchstudent,name='Searchstudent'),
    # path('editbookdetails/<int:id>',views.editbookdetails,name='editbookdetails'),
    # path('<int:id>/updatedetails/',views.updatedetails,name='updatedetails'),
    # path('addstudent/',views.addstudent,name='addstudent'),
    # path('addstudentsubmission/',views.addstudentsubmission,name='addstudentsubmission'),
    # path('viewissuedbook/',views.viewissuedbook,name='viewissuedbook'),
    # path('viewstudents/',views.viewstudents,name='viewstudents')

]