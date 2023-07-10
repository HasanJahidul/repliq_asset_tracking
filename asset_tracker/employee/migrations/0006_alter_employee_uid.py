# Generated by Django 4.2.3 on 2023-07-10 01:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_company_alter_employee_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('dd54a058-f893-441a-8eff-e0078268af96'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
