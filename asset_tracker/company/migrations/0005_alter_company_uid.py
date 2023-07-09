# Generated by Django 4.2.3 on 2023-07-09 22:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('48bf6910-9c16-4b32-8d80-fb55ac2a9ba2'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
