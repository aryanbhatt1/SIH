# Generated by Django 3.2.12 on 2022-03-13 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SIH', '0007_auto_20220313_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='form',
            name='Last_name',
        ),
        migrations.RemoveField(
            model_name='form',
            name='address',
        ),
        migrations.RemoveField(
            model_name='form',
            name='city',
        ),
        migrations.RemoveField(
            model_name='form',
            name='country',
        ),
        migrations.RemoveField(
            model_name='form',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='form',
            name='email',
        ),
        migrations.RemoveField(
            model_name='form',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='form',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='form',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='form',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='form',
            name='state',
        ),
    ]