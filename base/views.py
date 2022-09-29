from contextlib import redirect_stderr
from email import message
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Ticket, Student, Officer
from django.views.decorators.csrf import csrf_protect
from .forms import SignupStudent, LoginStudentForm, MyChangeFormPassword
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt
from .models import Users, StudentProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


class Login_student(TemplateView):
    template_name = 'student/login.html'


@csrf_protect
def login_student(request):
    if request.method == 'POST':
        print('test')
        form = LoginStudentForm(None, data=request.POST)
        print(request.POST)

        print("form is valid")
        # username = form.cleaned_data.get('username')
        username = request.POST['username']
        #print(email)
        # password = form.cleaned_data.get('password')
        password = request.POST['password']
        print(password)
        user = authenticate(username=username, password=password)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            if user is not None:
                login(request, user)
            
                messages.info(request, 'You have successfully logged in!')           
                return redirect('raise-ticket')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
# else:
#     messages.error(request, "Invalid email or password.")

    form = LoginStudentForm()

    return render(request, "student/login.html", {'form': form})



# class StudentSignUpView(CreateView):
#     model = Users
#     #fields = '__all__'
#     form_class = SignupStudent
#     template_name = 'student/register.html'


#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('raise-ticket')



@csrf_exempt
def register_student(request):  
    if request.method == 'POST':  
        form = SignupStudent(request.POST or None)  
        if form.is_valid():  
            form.save() 
            user = form.cleaned_data.get('username')
            messages.info(request, 'Account was created successfully for ' + user)
            return redirect('raise-ticket')
    else:  
        form = SignupStudent() 
    context = {  
        'form':form  
    }  
    return render(request, 'student/register.html', context) 




# @csrf_protect
# def register_student(request):
#     if request.method == 'GET':
#         form = SignupStudent()
#         context = {'form': form}
#         return render(request, 'student/register.html', context)
#     if request.method == 'POST':
#         form = SignupStudent(request.POST or None)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')
#             messages.success(request, 'Account was created for ' + user)
#             return redirect('raise-ticket')
#     else:
#         form = SignupStudent()
#         print('Form is invalid')
#         messages.error(request, 'Error Processing Your Request')
#         context = {'form': form}
#         return render(request, 'student/register.html', context)
#     # context={'form':form}
#     return render(request, 'student/register.html', {'form': SignupStudent})


class Register_officer(TemplateView):
    template_name = 'officer/register.html'


class Login_officer(TemplateView):
    template_name = 'officer/login.html'


class Login_admin(TemplateView):
    template_name = 'admin/login.html'


class Raise_Ticket(SuccessMessageMixin,CreateView):
    model = Ticket
    template_name = 'student/dashboard.html'
    success_message = "Ticket was created successfully"

    fields = ('ticket_name', 'ticket_type',
              'ticket_status', 'ticket_description',)


class My_Tickets(ListView):
    model = Ticket
    template_name = 'student/my_tickets.html'
    # fields = ('ticket_name', 'ticket_type', 'ticket_status',
    # 'ticket_description', 'created_at', 'updated_at')

    # def get_queryset(self):
    # return super().get_queryset().order_by(self.kwargs['ticket_id'])


class My_Account(ListView):
    model = StudentProfile
    template_name = 'student/my_account.html'
    context_object_name = 'students'
   
@login_required
def change_password(request):
    if request.method == 'POST':
        form = MyChangeFormPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('my-account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyChangeFormPassword(request.user)
    return render(request, 'student/change_password.html', {
        'form': form
    })


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



def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out of your account!')
    return redirect('home')