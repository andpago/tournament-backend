# Generated by Django 2.0.5 on 2018-05-03 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20180503_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='round',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='round.Round'),
        ),
    ]