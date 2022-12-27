from django.urls import path
from .views import *

urlpatterns = [
    path("", Index_Page.as_view(), name="index"),
    path('home', home_Page.as_view(), name="home"),
    path("add_book/", Create_Book.as_view(), name="add_book"),
    path("view_books/", Book_List.as_view(), name="view_books"),
    path("view_students/", Student_List.as_view(), name="view_students"),
    path("issue_book/", IssueBooks.as_view(), name="issue_book"),
    path("view_issued_book/", MyBookIsssued_view.as_view(), name="view_issued_book"),
    path("student_issued_books/", Student_Book_Issued.as_view(), name="student_issued_books"),
    path("profile/", Profile_View.as_view(), name="profile"),
    path("profile/<int:pk>", Update_User.as_view(), name="edit_profile"),

    #path("student_registration/", Register_Student.as_view(), name="student_registration"),
    #path("student_login/", student_login, name="student_login"),
   

    path("delete_book/<int:pk>/", Delete_Book.as_view(), name="delete_book"),
    path("delete_student/<int:pk>/", Delete_Student.as_view(), name="delete_student"),
]