from django.contrib import admin
from .models import Users, Student, Officer, Ticket
# Register your models here.
admin.site.register(Users)
#admin.site.register(Officer)
#admin.site.register(Ticket)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
     list_display = ('last_name', 'first_name', 'reg_no', 'email')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
     list_display = ('ticket_name', 'ticket_type', 'ticket_status')

@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
     list_display = ('last_name', 'first_name', 'email', 'phone_number')

#admin.site.register(Student,StudentAdmin)