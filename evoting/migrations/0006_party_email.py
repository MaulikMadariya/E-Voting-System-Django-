# Generated by Django 4.1.7 on 2023-06-07 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evoting', '0005_alter_party_pid_alter_party_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
