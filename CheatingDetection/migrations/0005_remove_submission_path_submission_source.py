# Generated by Django 4.2.4 on 2023-09-30 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheatingDetection', '0004_alter_submission_sub_id_alter_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='path',
        ),
        migrations.AddField(
            model_name='submission',
            name='source',
            field=models.CharField(default='', max_length=100000),
            preserve_default=False,
        ),
    ]