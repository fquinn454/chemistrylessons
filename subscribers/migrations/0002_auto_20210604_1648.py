# Generated by Django 3.2 on 2021-06-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('T', 'Teacher'), ('S', 'Student'), ('P', 'Parent')], default='T', max_length=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
