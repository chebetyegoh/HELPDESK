from datetime import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Users(AbstractUser):
   # id = models.AutoField(primary_key = True)
    #username = models.CharField(max_length=20, unique="True", blank=False)
    is_Student = models.BooleanField(default=False)
    is_Officer = models.BooleanField(default=False)


class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
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
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['ticket_name']

    def get_absolute_url(self):
        return reverse('my-tickets')

    def __str__(self):
        return f'{self.ticket_name}'
    


class Student(models.Model):

    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True, related_name = 'student_related_user')
    ticket = models.ForeignKey(Ticket, on_delete= models.CASCADE, related_name = 'student_related_ticket')
    reg_no = models.IntegerField(null=True, blank=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, null=True)
    last_name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(null=True, blank=False, unique=True)
    username = models.CharField(max_length= 200, null=True, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('login')

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'


class Officer(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True, related_name = 'officer_related_user')
    ticket = models.ForeignKey(Ticket, on_delete= models.CASCADE, related_name = 'officer_related_ticket')
    first_name = models.CharField(max_length=200, blank=False, null=True)
    last_name = models.CharField(max_length=200, blank=False, null=True)
    email = models.EmailField(null=True, blank=False, unique=True)
    phone_number = models.CharField(max_length=100, blank=False, null=True, unique=True)
    role = models.CharField(max_length=20, blank=False, null=True)
    officer_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

   #def get_absolute_url(self):
       # return reverse('officer-detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'