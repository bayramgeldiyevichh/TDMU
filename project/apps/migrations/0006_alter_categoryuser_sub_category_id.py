# Generated by Django 4.1.2 on 2022-10-20 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_categoryuser_sub_category_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryuser',
            name='sub_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cat', to='apps.subcategory'),
        ),
    ]
