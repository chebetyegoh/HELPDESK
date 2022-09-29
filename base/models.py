from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Users(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        OFFICER = "OFFICER", "Officer"

    # base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices, default='STUDENT' )

# @receiver(post_save, sender=Users)
# def create_user_profile(sender, instance, created, **kwargs):
#      if created:
#         instance.role.add('STUDENT')
    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.role = self.base_role
    #         return super().save(*args, **kwargs)
    
#    # id = models.AutoField(primary_key = True)
#     username = models.CharField(max_length=20, unique="True", blank=False)
#     is_student = models.BooleanField(default=False)
#     is_officer = models.BooleanField(default=False)


class StudentManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Users.Role.STUDENT)


class Student(Users):

    base_role = Users.Role.STUDENT

    student = StudentManager()

    class Meta:
        proxy = True




class StudentProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)










class OfficerManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=Users.Role.OFFICER)

class Officer(Users):

    base_role = Users.Role.OFFICER

    officer = OfficerManager()

    class Meta:
        proxy = True


class OfficerProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    officer_id = models.IntegerField(null=True, blank=True)
    phone_number = models.CharField(max_length=100, blank=False, null=True, unique=True)



@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
     if created and instance.role == "STUDENT":
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=Users)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "OFFICER":
        OfficerProfile.objects.create(user=instance)

# class Student(models.Model):

#     user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True, related_name = 'student_related_user')
#     first_name = models.CharField(max_length=200, blank=False, null=True)
#     last_name = models.CharField(max_length=200, blank=False, null=True)
#     email = models.EmailField(null=True, blank=False, unique=True)
#     username = models.CharField(max_length= 200, null=True, blank=False, default='stude')
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     updated_at = models.DateTimeField(default=datetime.now, blank=True)

#     class Meta:
#         ordering = ['last_name', 'first_name']

#     def get_absolute_url(self):
#         return reverse('login')

#     def __str__(self):
#         return f'{self.last_name}, {self.first_name}'


# class Officer(models.Model):
#     user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True, related_name = 'officer_related_user')
#     first_name = models.CharField(max_length=200, blank=False, null=True)
#     last_name = models.CharField(max_length=200, blank=False, null=True)
#     email = models.EmailField(null=True, blank=False, unique=True)
#     #username = models.CharField(max_length= 200, null=True, blank=False, default='stude')
#     phone_number = models.CharField(max_length=100, blank=False, null=True, unique=True)
#     created_at = models.DateTimeField(default=datetime.now, blank=True)
#     updated_at = models.DateTimeField(default=datetime.now, blank=True)

#     class Meta:
#         ordering = ['last_name', 'first_name']

#    #def get_absolute_url(self):
#        # return reverse('officer-detail', args=[str(self.id)])
#     def __str__(self):
#         return f'{self.last_name}, {self.first_name}'


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(Student, on_delete= models.CASCADE, null=True,related_name = 'created_by')
    closed_by = models.ForeignKey(Officer, on_delete= models.CASCADE, null=True, related_name = 'closed_by')
    ticket_name = models.CharField(max_length=200, blank=True)
    ticket_type = models.CharField(max_length=200, blank=True)
    ticket_description = models.TextField(max_length=200, blank=True)

    StatusChoices = [
        ('InProgress', 'InProgress'),
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Deferred', 'Deferred'),
    ]
    ticket_status = models.CharField(max_length=200, choices=StatusChoices,
        default= 'Open', blank=True)
    #reg_no = models.CharField(max_length=200, blank=False, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_by']

    def get_absolute_url(self):
        return reverse('my-tickets')

    def __str__(self):
        return f'{self.ticket_name}'
    