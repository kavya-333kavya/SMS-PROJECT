# Generated by Django 5.0 on 2024-02-02 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0007_alter_customuser_groups_alter_customuser_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
