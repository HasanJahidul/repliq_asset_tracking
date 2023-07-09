# Generated by Django 4.2.3 on 2023-07-09 22:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0002_alter_device_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('554109d1-4331-4df5-a335-662513d53942'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
