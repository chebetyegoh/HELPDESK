# Generated by Django 4.1.1 on 2022-09-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_ticket_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
