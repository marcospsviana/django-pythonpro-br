# Generated by Django 3.2.6 on 2021-09-04 16:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_alterado_tamanho_titulo_para_60'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]