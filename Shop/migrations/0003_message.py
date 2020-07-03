# Generated by Django 2.2.11 on 2020-03-20 17:13

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20200319_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('createdOn', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
