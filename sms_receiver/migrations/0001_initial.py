# Generated by Django 5.1.1 on 2024-09-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('national_code', models.CharField(max_length=10)),
                ('sms_code', models.CharField(max_length=10)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
