from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Users, OfficerProfile, Ticket, Officer, StudentProfile,Student
# Register your models here.
class UserTest(UserAdmin):
     model=Users
     fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
     list_display = ('username', 'role',)
admin.site.register(Users, UserTest)
#admin.site.register(Officer)
#admin.site.register(Ticket)


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
     list_display=('user','get_email','firstname','lastname','student_id')
     def get_email(self, obj):
        return obj.user.email
     def firstname(self,obj):
          return obj.user.first_name
     def lastname(self,obj):
          return obj.user.last_name


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
     list_display = ('ticket_name', 'ticket_type', 'ticket_status','created_by')

@admin.register(OfficerProfile)
class OfficerProfileAdmin(admin.ModelAdmin):
     list_display=('user','get_email','firstname','lastname', 'phone_number', 'id')
     def get_email(self, obj):
        return obj.user.email
     def firstname(self,obj):
          return obj.user.first_name
     def lastname(self,obj):
          return obj.user.last_name



#admin.site.register(Student,StudentAdmin)