# Generated by Django 4.2.1 on 2023-07-02 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0007_auto_20230702_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
