# Generated by Django 5.0.4 on 2024-05-19 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmsapp', '0008_alter_user_uploadfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uploadfile',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
