# Generated by Django 5.0 on 2024-02-02 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0002_alter_signin_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signin',
            old_name='Confirm_password',
            new_name='Confirmpassword',
        ),
        migrations.RenameField(
            model_name='signin',
            old_name='Password',
            new_name='password',
        ),
    ]
