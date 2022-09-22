from contextlib import redirect_stderr
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Ticket, Student, Officer
from .forms import Signup
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from .models import Users
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'




class Login_student(TemplateView):
    template_name = 'student/login.html'
@csrf_exempt
def login_student(request):
	if request.method == "POST":
		#form = AuthenticationForm(request, data=request.POST)
       
		# if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")               
                    
				return redirect("raise-ticket")
			else:
				messages.error(request,"Invalid username or password.")
		# else:
		# 	messages.error(request,"Invalid username or password.")
            
	# form = AuthenticationForm()
	return render(request, 'student/login.html')
@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        reg_no = request.POST['reg_no']
        re_pass = request.POST['re_pass']
        email = request.POST['email']
        if (password != re_pass):
            messages.error(request, "Password do not match")
        else:
            try:
                user = Users.objects.get(username=username)
            except:
                user = None
    
            
            if(user is not None):
                messages.error(request, 'User already exists')
            else:
                Users.objects.create(username=username, first_name=first_name, last_name=last_name, email=email, password=password, is_Student=True)
                
                messages.info(request, 'user registered')
                return redirect("login")

    return render(request, 'student/register.html')



class Register_officer(TemplateView):
    template_name = 'officer/register.html'


class Login_officer(TemplateView):
    template_name = 'officer/login.html'


class Login_admin(TemplateView):
    template_name = 'admin/login.html'


class Raise_Ticket(CreateView):
    model = Ticket
    template_name = 'student/dashboard.html'

    fields = ('ticket_name', 'ticket_type',
              'ticket_status', 'ticket_description')


class My_Tickets(ListView):
    model = Ticket
    template_name = 'student/my_tickets.html'
    # fields = ('ticket_name', 'ticket_type', 'ticket_status',
    # 'ticket_description', 'created_at', 'updated_at')

    # def get_queryset(self):
    # return super().get_queryset().order_by(self.kwargs['ticket_id'])


class My_Account(TemplateView):
    template_name = 'student/my_account.html'


class Change_Password(TemplateView):
    template_name = 'student/change_password.html'


class Officer_Dashboard(TemplateView):
    template_name = 'officer/dashboard.html'


class Officer_Tickets(ListView):
    model = Ticket
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


class Ticket_view(DetailView):
    template_name = 'student/view_ticket.html'
    model = Ticket
    context_object_name = 'tickets'


class Close_Ticket(DetailView):
    model = Ticket
    template_name = 'officer/close_ticket.html'
    context_object_name = 'tickets'