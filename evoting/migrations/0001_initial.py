# Generated by Django 4.1.7 on 2023-06-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('password', models.TextField(max_length=20)),
                ('cpassword', models.TextField(max_length=20)),
                ('address', models.TextField(max_length=100)),
                ('number', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('panNumber', models.TextField(max_length=10)),
                ('aadharNumber', models.TextField(max_length=12)),
            ],
            options={
                'db_table': 'evoting_username',
            },
        ),
    ]
