# Generated by Django 4.1.2 on 2022-10-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_remove_questions_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='description',
            field=models.FileField(blank=True, null=True, upload_to='descriptions'),
        ),
    ]