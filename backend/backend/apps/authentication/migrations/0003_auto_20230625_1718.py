# Generated by Django 3.2.19 on 2023-06-25 14:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20230625_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryman',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='options_deliveryman', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='options_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
