# Generated by Django 4.2.7 on 2023-11-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hr_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_employees',
            name='Emp_Id',
            field=models.BigIntegerField(null=True),
        ),
    ]
