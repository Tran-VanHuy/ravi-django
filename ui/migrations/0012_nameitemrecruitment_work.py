# Generated by Django 5.0.6 on 2024-09-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0011_alter_itemnameitemrecruitment_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='nameitemrecruitment',
            name='work',
            field=models.CharField(blank=True, choices=[('FULL TIME', 'FULL TIME'), ('PART TIME', 'PART TIME')], max_length=255, null=True, verbose_name='work'),
        ),
    ]
