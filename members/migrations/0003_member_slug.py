# Generated by Django 4.2.16 on 2024-10-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
