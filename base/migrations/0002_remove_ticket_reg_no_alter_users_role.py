# Generated by Django 4.1.1 on 2022-09-29 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='reg_no',
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('STUDENT', 'Student'), ('OFFICER', 'Officer')], default='STUDENT', max_length=50),
        ),
    ]
