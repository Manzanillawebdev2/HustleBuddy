# Generated by Django 3.1.6 on 2021-08-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMIList', '0011_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.AddField(
            model_name='signup',
            name='meyl',
            field=models.EmailField(default='', max_length=50, verbose_name='meyl'),
        ),
    ]
