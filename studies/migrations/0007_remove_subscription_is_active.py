# Generated by Django 4.2 on 2024-03-20 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0006_alter_subscription_course_alter_subscription_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='is_active',
        ),
    ]
