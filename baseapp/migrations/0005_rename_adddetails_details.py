# Generated by Django 4.2.6 on 2023-10-16 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0004_rename_yviews_adddetails_what_users_say_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addDetails',
            new_name='Details',
        ),
    ]
