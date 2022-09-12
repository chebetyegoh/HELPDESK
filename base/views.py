from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

class Register_student(TemplateView):
    template_name = 'student/register.html'

class Login_student(TemplateView):
    template_name = 'student/login.html'

class Register_officer(TemplateView):
    template_name = 'officer/register.html'

class Login_officer(TemplateView):
    template_name = 'officer/login.html'

class Login_admin(TemplateView):
    template_name = 'admin/login.html'

class Raise_Ticket(TemplateView):
    template_name = 'student/dashboard.html'

class My_Tickets(TemplateView):
    template_name = 'student/my_tickets.html'

class My_Account(TemplateView):
    template_name = 'student/my_account.html'

class Change_Password(TemplateView):
    template_name = 'student/change_password.html'


