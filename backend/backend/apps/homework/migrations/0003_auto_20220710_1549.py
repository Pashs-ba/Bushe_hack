# Generated by Django 3.2.13 on 2022-07-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0002_alter_homeworkattachment_homework'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['lesson__date'], 'verbose_name': 'Домашнее задание', 'verbose_name_plural': 'Домашние задания'},
        ),
        migrations.AlterField(
            model_name='homeworkattachment',
            name='homework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='homework.homework'),
        ),
    ]
