# Generated by Django 4.1 on 2022-09-05 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mchath', '0002_remove_quiz_no_remove_quiz_yes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setup',
            name='caregiver_name',
            field=models.OneToOneField(max_length=200, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
