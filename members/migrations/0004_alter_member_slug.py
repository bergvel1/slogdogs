# Generated by Django 4.2.16 on 2024-10-25 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
