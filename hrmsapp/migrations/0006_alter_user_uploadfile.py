# Generated by Django 5.0.4 on 2024-05-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0005_alter_user_econtact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uploadfile',
            field=models.FileField(blank=True, null=True, upload_to='uploadfile/'),
        ),
    ]
