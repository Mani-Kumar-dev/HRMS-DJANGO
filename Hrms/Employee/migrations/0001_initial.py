# Generated by Django 4.2.7 on 2023-11-11 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Last_Name', models.CharField(max_length=50)),
                ('Emp_Id', models.IntegerField(default=0)),
                ('Designation', models.CharField(max_length=100)),
                ('Contact', models.BigIntegerField()),
                ('Email', models.CharField(max_length=150)),
                ('Location', models.CharField(max_length=100)),
                ('Salary', models.BigIntegerField(default=0)),
            ],
        ),
    ]
