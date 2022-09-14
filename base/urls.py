from re import L
from django.urls import path
from .views import Home, Register_student, Login_student, Register_officer,Login_officer,Login_admin,Raise_Ticket,My_Tickets,My_Account,Change_Password,Officer_Dashboard, Officer_Tickets,Officer_Account,Officer_Change_Password,Admin_Dashboard,Admin_Ticket_Report,Admin_Change_Password,Register_Officer,Officers_List,Admin_Student_report,About,Services

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
    path('officer-dashboard', Officer_Dashboard.as_view()),
    path('officer-tickets', Officer_Tickets.as_view()),
    path('officer-account', Officer_Account.as_view()),
    path('officer-change-password',Officer_Change_Password.as_view()),
    path('admin-dashboard', Admin_Dashboard.as_view()),
    path('ticket-report', Admin_Ticket_Report.as_view()),
    path('admin-change-password', Admin_Change_Password.as_view()),
    path('create-officer-account', Register_Officer.as_view()),
    path('officers-list', Officers_List.as_view()),
    path('student-report', Admin_Student_report.as_view()),
    path('about', About.as_view()),
    path('services', Services.as_view()),
]