# Generated by Django 5.0 on 2024-02-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='birthdate',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
