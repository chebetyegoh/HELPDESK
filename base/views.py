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

class Officer_Dashboard(TemplateView):
    template_name = 'officer/dashboard.html'

class Officer_Tickets(TemplateView):
    template_name = 'officer/tickets.html'

class Officer_Account(TemplateView):
    template_name = 'officer/my_account.html'

class Officer_Change_Password(TemplateView):
    template_name = 'officer/change_password.html'

class Admin_Dashboard(TemplateView):
    template_name = 'admin/dashboard.html'

class Admin_Ticket_Report(TemplateView):
    template_name = 'admin/ticket_report.html'

class Admin_Change_Password(TemplateView):
    template_name = 'admin/change_password.html'

class Register_Officer(TemplateView):
    template_name = 'admin/register_officer.html'

class Officers_List(TemplateView):
    template_name = 'admin/officers_list.html'

class Admin_Student_report(TemplateView):
    template_name = 'admin/student_report.html'

class About(TemplateView):
    template_name = 'about.html'


class Services(TemplateView):
    template_name = 'service.html'

class Contact_us(TemplateView):
    template_name = 'contact_us.html'

class Terms(TemplateView):
    template_name = 'terms.html'

class Graph(TemplateView):
    template_name = 'admin/graph.html'
    

class Ticket(TemplateView):
    template_name = 'student/view_ticket.html'

class Close_Ticket(TemplateView):
    template_name = 'officer/close_ticket.html'
