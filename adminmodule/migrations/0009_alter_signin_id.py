# Generated by Django 5.0 on 2024-02-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminmodule', '0008_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
