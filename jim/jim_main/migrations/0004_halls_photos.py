# Generated by Django 4.2 on 2023-05-01 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jim_main', '0003_halls_title_alter_trenings_dt_alter_trenings_hall_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='halls',
            name='photos',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
