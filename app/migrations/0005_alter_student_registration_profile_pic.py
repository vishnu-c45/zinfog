# Generated by Django 4.0.4 on 2022-11-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_admin_registration_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_registration',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
