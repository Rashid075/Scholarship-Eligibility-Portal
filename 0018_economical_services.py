# Generated by Django 4.2.1 on 2023-07-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0017_remove_sport_services_service1_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Economical_Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service2_name', models.CharField(max_length=122)),
                ('service2_amount', models.CharField(max_length=122)),
                ('service3_eligibility', models.CharField(max_length=122)),
            ],
        ),
    ]