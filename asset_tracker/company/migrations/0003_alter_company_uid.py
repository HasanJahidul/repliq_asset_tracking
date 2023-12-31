# Generated by Django 4.2.3 on 2023-07-09 22:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_alter_company_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('ccf829e4-a496-425d-9306-afd99a4e72d1'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
