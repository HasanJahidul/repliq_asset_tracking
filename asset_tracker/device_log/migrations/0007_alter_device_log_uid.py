# Generated by Django 4.2.3 on 2023-07-10 02:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('device_log', '0006_alter_device_log_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_log',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('5310cbbc-71a8-4622-8c97-135ecfba5bf2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
