# Generated by Django 4.2.3 on 2023-07-10 03:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_alter_company_uid'),
        ('device', '0008_device_company_alter_device_belongs_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='belongs_to',
        ),
        migrations.AlterField(
            model_name='device',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='company.company'),
        ),
        migrations.AlterField(
            model_name='device',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('67bf8023-de6b-40b7-af44-9e154510c8d2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
