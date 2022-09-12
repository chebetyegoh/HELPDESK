from re import L
from django.urls import path
from .views import Home, Register_student, Login_student, Register_officer,Login_officer,Login_admin,Raise_Ticket,My_Tickets,My_Account,Change_Password

urlpatterns =[
    path('', Home.as_view()),
    path('register', Register_student.as_view()),
    path('login', Login_student.as_view()),
    path('register-officer', Register_officer.as_view()),
    path('login-officer', Login_officer.as_view()),
    path('login-admin',Login_admin.as_view()),
    path('raise-ticket', Raise_Ticket.as_view()),
    path('my-tickets', My_Tickets.as_view()),
    path('my-account', My_Account.as_view()),
    path('change-password', Change_Password.as_view()),

]