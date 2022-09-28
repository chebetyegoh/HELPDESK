from django.contrib import admin
from .models import Users, OfficerProfile, Ticket, Officer, StudentProfile,Student
# Register your models here.
admin.site.register(Users)
#admin.site.register(Officer)
#admin.site.register(Ticket)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
     list_display=('user','get_email','firstname','lastname',)
     def get_email(self, obj):
        return obj.user.email
     def firstname(self,obj):
          return obj.user.first_name
     def lastname(self,obj):
          return obj.user.last_name


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
     list_display = ('ticket_name', 'ticket_type', 'ticket_status')

@admin.register(OfficerProfile)
class OfficerProfileAdmin(admin.ModelAdmin):
     list_display=('user','get_email','firstname','lastname', 'phone_number')
     def get_email(self, obj):
        return obj.user.email
     def firstname(self,obj):
          return obj.user.first_name
     def lastname(self,obj):
          return obj.user.last_name

#admin.site.register(Student,StudentAdmin)