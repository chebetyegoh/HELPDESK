from contextlib import redirect_stderr
from email import message
from multiprocessing import context

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import OfficerProfile, Ticket, Student, Officer
from django.views.decorators.csrf import csrf_protect
from .forms import SignupStudent, LoginStudentForm, MyChangeFormPassword, EditProfile, RaiseTicketForm, LoginOfficerForm, LoginAdminForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_exempt
from .models import Users, StudentProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.core.mail import send_mail
from django.conf import settings

# from django import form
# Create your views here.


class Home(TemplateView):
    template_name = 'home.html'


# @csrf_protect
@csrf_exempt
def login_student(request):
    if request.method == 'POST':
        print('test')
        form = LoginStudentForm(None, data=request.POST)
        print(request.POST)

        print("form is valid")
        # username = form.cleaned_data.get('username')
        username = request.POST['username']
        # print(email)
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
                messages.error(request, "Invalid username or password.")
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
            messages.info(
                request, 'Account was created successfully for ' + user)
            return redirect('login')
    else:
        form = SignupStudent()
    context = {
        'form': form
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


@csrf_exempt
def login_officer(request):
    if request.method == 'POST':
        print('test')
        form = LoginOfficerForm(None, data=request.POST)
        print(request.POST)

        print("form is valid")
        # username = form.cleaned_data.get('username')
        username = request.POST['username']
        # print(email)
        # password = form.cleaned_data.get('password')
        password = request.POST['password']
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            type_obj = Users.objects.get(username=user.username)
            print(type_obj)
            if user.is_authenticated:
                messages.info(request, 'You have successfully logged in!')
                return redirect('officer-dashboard')
        else:
            # Invalid email or password. Handle as you wish
            messages.error(request, "Invalid username or password.")

# else:
#     messages.error(request, "Invalid email or password.")

    form = LoginOfficerForm()

    return render(request, "officer/login.html", {'form': form})


@csrf_exempt
def login_admin(request):
    if request.method == 'POST':
        print('test')
        form = LoginAdminForm(None, data=request.POST)
        print(request.POST)

        print("form is valid")
        # username = form.cleaned_data.get('username')
        username = request.POST['username']
        # print(email)
        # password = form.cleaned_data.get('password')
        password = request.POST['password']
        print(password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            type_obj = Users.objects.get(username=user.username)
            print(type_obj)
            if user.is_authenticated:
                messages.info(request, 'You have successfully logged in!')
                return redirect('admin-dashboard')
        else:
            # Invalid email or password. Handle as you wish
            messages.error(request, "Invalid username or password.")

# else:
#     messages.error(request, "Invalid email or password.")

    form = LoginAdminForm()

    return render(request, "administrator/login22.html", {'form': form})


class Login_admin(TemplateView):
    template_name = 'administrator/login.html'


# @csrf_exempt
# def raise_ticket(request):
#     if request.method == 'POST':
#         form = RaiseTicketForm(request.POST or None)
#         if form.is_valid():
#             form.save(commit=False)
#             form.user = request.user
#             form.save()
#             messages.info(
#                 request, 'Ticket was created successfully')
#             return redirect('my-tickets')
#     else:
#         form = RaiseTicketForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'student/dashboard.html', context)


@csrf_exempt
def raise_ticket(request):
    if request.method == 'POST':
        form = RaiseTicketForm(request.POST or None)

        if form.is_valid():
            reg_no = request.POST['reg_no']
            subject = "Ticket was created"
            message = f'Hello A ticket from { reg_no } has been created'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['asaliasali346@gmail.com']
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            ticket = form.save(commit=False)
            stu_obj = get_object_or_404(StudentProfile, user=request.user)
            ticket.created_by = stu_obj
            ticket.save()
            messages.info(
                request, 'Ticket was created successfully')
            return redirect('raise-ticket')
    else:
        form = RaiseTicketForm()
    context = {
        'form': form
    }
    return render(request, 'student/dashboard.html', context)

# @csrf_exempt
# def raise_ticket(request):

#     if request.method == 'POST':
#         ticket_name = request.POST['ticket_name']

#         ticket_post = RaiseTicketForm(request.POST or None)
#         if ticket_post.is_valid():
#             ticket = ticket_post.save(commit=False)
#             ticket.created_by = request.user
#             print(request.user)
#             ticket.save()
#             messages.info(
#                     request, 'Ticket was created successfully')
#             return redirect('my-tickets')
#     else:
#         form = RaiseTicketForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'student/dashboard.html', context)


# class Raise_Ticket(SuccessMessageMixin, CreateView):
#     model = Ticket
#     template_name = 'student/dashboard.html'
#     success_message = "Ticket was created successfully"

#     fields = ('ticket_name', 'ticket_type',
#               'ticket_status', 'ticket_description',)


class My_Tickets(ListView):
    model = Ticket
    template_name = 'student/my_tickets.html'

    # fields = ('ticket_name', 'ticket_type', 'ticket_status',
    # 'ticket_description', 'created_at', 'updated_at')

    # def get_queryset(self):
    # return super().get_queryset().order_by(self.kwargs['ticket_id'])


def listTickets(request, username):
    owner = Users.objects.get(username=username)
    id = StudentProfile.objects.get(user=owner.id).student_id
    my_tickets = Ticket.objects.filter(created_by=id)
    context = {
        "object_list": my_tickets
    }
    return render(request, 'student/my_tickets.html', context)


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
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('my-account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyChangeFormPassword(request.user)
    return render(request, 'student/change_password.html', {
        'form': form
    })


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid:
            form.save()
            messages.info(
                request, 'Your profile was updated successfully!')
            return redirect('my-account')
    else:
        form = EditProfile(instance=request.user)
        args = {
            'form': form,
        }
        return render(request, 'student/updateprofile.html', args)


class UpdateProfile(UpdateView):
    model = Users
    fields = ['first_name', 'last_name', 'email', 'username']
    template_name = 'student/updateprofile.html'


class TicketUpdate(UpdateView):
    model = Ticket
    fields = ['ticket_name', 'ticket_type', 'ticket_description', ]
    template_name = 'student/updateticket.html'
    success_url = reverse_lazy("raise-ticket")


class DeleteConfirmation(ListView):
    template_name = 'student/ticket_delete.html'
    model = Ticket


class Ticketdeleteview(DeleteView):
    model = Ticket
    template_name = "student/ticket_delete.html"
    success_url = reverse_lazy("raise-ticket")


class Ticket_view(DetailView):
    template_name = 'student/view_ticket.html'
    model = Ticket
    context_object_name = 'tickets'


def officer_dashboard(request):
    ticket_count = Ticket.objects.all().count()
    open_tickets = Ticket.objects.filter(ticket_status='Open').count()
    closed_tickets = Ticket.objects.filter(ticket_status='Closed').count()
    if ticket_count == 0:
        ticket_resolution = 0
    else:
        ticket_resolution = int((closed_tickets/ticket_count)*100)
    context = {
        'open_tickets': open_tickets,
        'ticket_count': ticket_count,
        'closed_tickets': closed_tickets,
        'ticket_resolution': ticket_resolution,
    }
    return render(request, 'officer/dashboard.html', context=context)


@login_required
def change_password_officer(request):
    if request.method == 'POST':
        form = MyChangeFormPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('officer-account')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyChangeFormPassword(request.user)
    return render(request, 'officer/change_password.html', {
        'form': form
    })


class Officer_Tickets(ListView):
    model = Ticket
    template_name = 'officer/tickets.html'


class Open_Tickets(ListView):
    model = Ticket
    template_name = 'officer/open_tickets.html'


class OfficerTicketdeleteview(ListView):
    model = Ticket
    template_name = "officer/delete_ticket.html"


class OfficerTicketdeleteview(DeleteView):
    model = Ticket
    template_name = "officer/delete_ticket.html"
    success_url = reverse_lazy("officer-tickets")


class Close_Ticket(DetailView):
    model = Ticket
    template_name = 'officer/close_ticket.html'
    context_object_name = 'tickets'


# def close_ticket(request, pk):
#     ticket = Ticket.objects.get(ticket_id=pk)
#     if request.method == "POST":
#         ticket = Ticket.objects.get(ticket_id=pk)
#         ticket.ticket_status = "Closed"
#         officer_obj = get_object_or_404(OfficerProfile, user=request.user)
#         ticket.closed_by = officer_obj
#         ticket.save()
#         tickets = Ticket.objects.all()
#         context = {
#             "object_list": tickets
#         }
#         return render(request, 'officer/tickets.html', context)
#     context = {
#         "tickets": ticket
#     }

#     return render(request, 'officer/close_ticket.html', context)


def close_ticket(request, pk):
    ticket = Ticket.objects.get(ticket_id=pk)
    if request.method == "POST":
        subject = "Ticket Closure"
        message = f'Your issue was solved and ticket was close'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['asaliasali346@gmail.com']
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        ticket = Ticket.objects.get(ticket_id=pk)
        ticket.ticket_status = "Closed"
        officer_obj = get_object_or_404(OfficerProfile, user=request.user)
        ticket.closed_by = officer_obj
        ticket.save()
        tickets = Ticket.objects.all()
        context = {
            "object_list": tickets
        }
        return render(request, 'officer/tickets.html', context)
    context = {
        "tickets": ticket
    }

    return render(request, 'officer/close_ticket.html', context)

# def close_ticket(request, pk):
#     ticket = Ticket.objects.get(ticket_id=pk)
#     if request.method == "POST":
#         ticket = Ticket.objects.get(ticket_id=pk)
#         ticket.ticket_status = "Closed"
#         # ticket.save()
#         officer_obj = get_object_or_404(OfficerProfile, user=request.user)
#         ticket = officer_obj
#         ticket.save()
#         tickets = Ticket.objects.all()

#         context = {
#             "object_list": tickets
#         }
#         messages.info(
#             request, 'Ticket was closed successfully')
#         return render(request, 'officer/tickets.html', context)
#     context = {
#         "tickets": ticket
#     }

#     return render(request, 'officer/close_ticket.html', context)


class Officer_Account(ListView):
    model = OfficerProfile
    template_name = 'officer/my_account.html'
    context_object_name = 'officers'


class Officer_Change_Password(TemplateView):
    template_name = 'officer/change_password.html'


def admin_dashboard(request):
    ticket_count = Ticket.objects.all().count()
    open_tickets = Ticket.objects.filter(ticket_status='Open').count()
    closed_tickets = Ticket.objects.filter(ticket_status='Closed').count()
    if ticket_count == 0:
        ticket_resolution = 0
    else:
        ticket_resolution = int((closed_tickets/ticket_count)*100)
    
    context = {
        'open_tickets': open_tickets,
        'ticket_count': ticket_count,
        'closed_tickets': closed_tickets,
        'ticket_resolution': ticket_resolution,
    }
    return render(request, 'administrator/dashboard.html', context=context)


@login_required
def change_password_admin(request):
    if request.method == 'POST':
        form = MyChangeFormPassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('admin-dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = MyChangeFormPassword(request.user)
    return render(request, 'administrator/change_password.html', {
        'form': form
    })


class Graph(TemplateView):
    template_name = 'administrator/graph.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["open"] = Ticket.objects.filter(ticket_status = 'Open').count()
        context["closed"] = Ticket.objects.filter(ticket_status = 'Closed').count()
        print(context)
        return context


def graph(request):
    open_tickets_json = serializers.serialize("json", Ticket.objects.filter(ticket_status='Open'), ensure_ascii=False)
    open_tickets = len(open_tickets_json)
    closed_tickets_json = serializers.serialize("json", Ticket.objects.filter(ticket_status='Closed'), ensure_ascii=False)
    closed_tickets = len(closed_tickets_json)
    
    context = {
        'open_ticket': open_tickets,
        'closed_tickets': closed_tickets,
    }
    return render(request,  'administrator/graph.html', context)

class Admin_Ticket_Report(ListView):
    model = Ticket
    template_name = 'administrator/ticket_report.html'

    


class Admin_Change_Password(TemplateView):
    template_name = 'administrator/change_password.html'


class Register_Officer(TemplateView):
    template_name = 'administrator/register_officer.html'


class Officers_List(ListView):
    model = OfficerProfile
    template_name = 'administrator/officers_list.html'


class Admin_Student_report(ListView):
    model = StudentProfile
    template_name = 'administrator/student_report.html'


class AdminTicketdeleteview(ListView):
    model = Ticket
    template_name = "administrator/delete_ticket.html"


class AdminStudentdeleteview(ListView):
    model = Users
    template_name = "administrator/delete_student.html"


class AdminStudentdeleteview(DeleteView):
    model = Users
    template_name = "administrator/delete_student.html"
    success_url = reverse_lazy("student-report")


class AdminTicketdeleteview(DeleteView):
    model = Ticket
    template_name = "administrator/delete_ticket.html"
    success_url = reverse_lazy("ticket-report")


class About(TemplateView):
    template_name = 'about.html'


class Services(TemplateView):
    template_name = 'service.html'


class Contact_us(TemplateView):
    template_name = 'contact_us.html'


class Terms(TemplateView):
    template_name = 'terms.html'

class Help(TemplateView):
    template_name = 'help.html'


# def delete_ticket(request,pk):
#     ticket_to_delete=Ticket.objects.get(ticket_id=pk)
#     ticket_to_delete.delete()
#     return redirect('raise-ticket')

def delete_ticket(request, pk):
    obj = get_object_or_404(Ticket, ticket_id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('raise-ticket')
    context = {
        "object": obj
    }
    return render(request, "student/ticket_delete.html", context)


def logout_view(request):
    logout(request)
    messages.info(request, 'You are logged out of your account!')
    return redirect('home')


# json_serializer = serializers.get_serializer("json")()

tickets_json = serializers.serialize("json", Ticket.objects.filter(ticket_status='Open'), ensure_ascii=False)
open_ticket = len(tickets_json)

# open_tickets = json_serializer.serialize(len(Ticket.objects.filter(ticket_status='Open')), ensure_ascii=False)