# Generated by Django 4.2 on 2023-05-01 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jim_main', '0002_treners_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='halls',
            name='title',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='trenings',
            name='dt',
            field=models.DateTimeField(verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='trenings',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jim_main.halls', verbose_name='Зал'),
        ),
        migrations.AlterField(
            model_name='trenings',
            name='trener',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='jim_main.treners', verbose_name='Тренер'),
        ),
        migrations.AlterField(
            model_name='trenings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Юзер'),
        ),
    ]
