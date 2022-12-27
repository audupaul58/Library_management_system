from django.urls import path
from .views import *

urlpatterns = [
    path("student_registration/", Register_Student.as_view(), name="student_registration"),
    path("admin_login/", LoginPage.as_view(), name="admin_login"),
    path("logout/", Logout, name="logout"),
    path("change_password/", change_password, name="change_password"),
    
    #path('login/', LoginPage.as_view(), name='login'),
   
    
]