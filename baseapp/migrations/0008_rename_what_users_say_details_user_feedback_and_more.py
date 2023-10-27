# Generated by Django 4.2.6 on 2023-10-27 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0007_alter_details_if_selected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='What_Users_Say',
            new_name='User_feedback',
        ),
        migrations.RenameField(
            model_name='details',
            old_name='if_selected',
            new_name='contact_via_email',
        ),
        migrations.AddField(
            model_name='details',
            name='contact_via_phone',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
