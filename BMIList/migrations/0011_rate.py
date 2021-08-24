# Generated by Django 3.1.6 on 2021-08-22 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BMIList', '0010_auto_20210817_0319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.TextField(default='')),
                ('Message', models.TextField(default='')),
                ('SignUp', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='BMIList.signup')),
            ],
        ),
    ]