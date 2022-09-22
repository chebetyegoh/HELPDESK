from re import L
from django.urls import path
from .views import Home, register_student, Login_student, Register_officer,Login_officer,Login_admin, Raise_Ticket,My_Tickets,My_Account,Change_Password,Officer_Dashboard, Officer_Tickets,Officer_Account,Officer_Change_Password,Admin_Dashboard,Admin_Ticket_Report,Admin_Change_Password,Register_Officer,Officers_List,Admin_Student_report,About,Services,Contact_us,Terms,Graph,Ticket_view,Close_Ticket
from . import views
urlpatterns =[
    
    path('', Home.as_view(), name='home'),
    path('register/', views.register_student, name='register'),
    path('login/', views.login_student, name='login'),
    path('register-officer', Register_officer.as_view(), name='register-officer'),
    path('login-officer', Login_officer.as_view(), name='login-officer'),
    path('login-admin',Login_admin.as_view(), name='login-admin'),
    path('raise-ticket', Raise_Ticket.as_view(), name='raise-ticket'),
    path('my-tickets', My_Tickets.as_view(), name='my-tickets'),
    path('my-account', My_Account.as_view(), name='my-account'),
    path('change-password', Change_Password.as_view(),name='change-password'),
    path('officer-dashboard', Officer_Dashboard.as_view(), name='officer-dashboard'),
    path('officer-tickets', Officer_Tickets.as_view(), name='officer-tickets'),
    path('officer-account', Officer_Account.as_view(), name='officer-account'),
    path('officer-change-password',Officer_Change_Password.as_view(), name='officer-change-password'),
    path('admin-dashboard', Admin_Dashboard.as_view(),name='admin-dashboard'),
    path('ticket-report', Admin_Ticket_Report.as_view(), name='ticket-report'),
    path('admin-change-password', Admin_Change_Password.as_view(), name='admin-change-password'),
    path('create-officer-account', Register_Officer.as_view(), name='create-officer-account'),
    path('officers-list', Officers_List.as_view(), name='officers-list'),
    path('student-report', Admin_Student_report.as_view(), name='student-report'),
    path('about', About.as_view(), name='about'),
    path('services', Services.as_view(), name='services'),
    path('contact', Contact_us.as_view(), name='contact'),
    path('terms', Terms.as_view(), name='terms'),
    path('graph',Graph.as_view(), name='graph'),
    path('ticket/<int:pk>', Ticket_view.as_view(), name='ticket'),
    path('close-ticket/<int:pk>', Close_Ticket.as_view(), name='close-ticket'),
                                                             
]