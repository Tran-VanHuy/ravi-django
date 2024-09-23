# Generated by Django 5.0.6 on 2024-09-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0036_alter_aboutme_image_alter_apply_resume_cv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='apply',
            name='resume_cv',
            field=models.FileField(unique=True, upload_to='images/cv', verbose_name='Resume/CV'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='itempartner',
            name='image',
            field=models.FileField(unique=True, upload_to='images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='itemproject',
            name='image',
            field=models.FileField(unique=True, upload_to='images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='recruitment',
            name='image',
            field=models.FileField(unique=True, upload_to='images', verbose_name='image'),
        ),
    ]
