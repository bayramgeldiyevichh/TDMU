# Generated by Django 4.1.2 on 2022-10-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_remove_questions_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='songs',
            field=models.FileField(blank=True, null=True, upload_to='songs'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]