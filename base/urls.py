from re import L
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns =[
    
    path('', views.Home.as_view(), name='home'),
    path('register/', views.register_student, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_student, name='login'),
    path('register-officer/', views.Register_officer.as_view(), name='register-officer'),
    path('login-officer/', views.Login_officer.as_view(), name='login-officer'),
    path('login-admin/',views.Login_admin.as_view(), name='login-admin'),
    path('raise-ticket/', login_required(views.Raise_Ticket.as_view()), name='raise-ticket'),
    path('my-tickets/', login_required(views.My_Tickets.as_view()), name='my-tickets'),
    path('my-account/', login_required(views.My_Account.as_view()), name='my-account'),
    path('change-password/', views.change_password,name='change-password'),
    path('officer-dashboard/', views.Officer_Dashboard.as_view(), name='officer-dashboard'),
    path('officer-tickets/', views.Officer_Tickets.as_view(), name='officer-tickets'),
    path('officer-account/', views.Officer_Account.as_view(), name='officer-account'),
    path('officer-change-password/',views.Officer_Change_Password.as_view(), name='officer-change-password'),
    path('admin-dashboard/', views.Admin_Dashboard.as_view(),name='admin-dashboard'),
    path('ticket-report/', views.Admin_Ticket_Report.as_view(), name='ticket-report'),
    path('admin-change-password/', views.Admin_Change_Password.as_view(), name='admin-change-password'),
    path('create-officer-account/', views.Register_Officer.as_view(), name='create-officer-account'),
    path('officers-list/', views.Officers_List.as_view(), name='officers-list'),
    path('student-report/', views.Admin_Student_report.as_view(), name='student-report'),
    path('about/', views.About.as_view(), name='about'),
    path('services/', views.Services.as_view(), name='services'),
    path('contact/', views.Contact_us.as_view(), name='contact'),
    path('terms/', views.Terms.as_view(), name='terms'),
    path('graph/',views.Graph.as_view(), name='graph'),
    path('ticket/<int:pk>/', views.Ticket_view.as_view(), name='ticket'),
    path('close-ticket/<int:pk>/', views.Close_Ticket.as_view(), name='close-ticket'),
                                                             
]