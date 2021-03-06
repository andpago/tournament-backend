# Generated by Django 2.0.5 on 2018-05-04 08:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('round', '0002_auto_20180503_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='round',
            name='is_final',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='round',
            name='is_selection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='round',
            name='participants',
            field=models.ManyToManyField(related_name='rounds', to=settings.AUTH_USER_MODEL),
        ),
    ]
