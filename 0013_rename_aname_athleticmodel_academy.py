# Generated by Django 4.2.1 on 2023-07-02 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0012_athleticmodel_rename_clgname_meritmodel_clgname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='athleticmodel',
            old_name='aname',
            new_name='academy',
        ),
    ]
