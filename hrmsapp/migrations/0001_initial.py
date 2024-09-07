# Generated by Django 5.0.4 on 2024-05-19 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tblevents',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=100)),
                ('efirstname', models.CharField(max_length=100)),
                ('elastname', models.CharField(blank=True, max_length=100, null=True)),
                ('edepartment', models.CharField(blank=True, max_length=50, null=True)),
                ('edesignation', models.CharField(blank=True, max_length=50, null=True)),
                ('leavetype', models.CharField(max_length=100)),
                ('econtact', models.IntegerField(blank=True, null=True)),
                ('noofdays', models.DateField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
