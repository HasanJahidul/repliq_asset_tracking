# Generated by Django 4.2.3 on 2023-07-10 02:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_company_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('f87f1c5f-b631-4c8d-8cb9-c8f1dd3a5e25'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
