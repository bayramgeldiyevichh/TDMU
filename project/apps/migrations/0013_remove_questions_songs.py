# Generated by Django 4.1.2 on 2022-10-24 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0012_questions_songs_alter_questions_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='songs',
        ),
    ]