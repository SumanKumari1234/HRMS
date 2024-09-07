# Generated by Django 5.0.4 on 2024-05-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0014_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplinary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100)),
                ('employee_code', models.IntegerField(unique=True)),
                ('disciplinary_action', models.TextField()),
                ('date_of_action', models.DateField()),
                ('disciplinary_notes', models.TextField()),
            ],
            options={
                'db_table': 'disciplinary',
            },
        ),
    ]
