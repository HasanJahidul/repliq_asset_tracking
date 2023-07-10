# Generated by Django 4.2.3 on 2023-07-10 01:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('device_log', '0004_alter_device_log_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_log',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('d70eb34f-b25b-4b91-81ed-7f4377a168b8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
