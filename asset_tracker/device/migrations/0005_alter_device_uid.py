# Generated by Django 4.2.3 on 2023-07-10 01:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0004_alter_device_belongs_to_alter_device_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('529033cc-2aa8-4dfd-8c1e-fb89f882b8c8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]