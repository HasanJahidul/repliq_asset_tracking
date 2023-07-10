# Generated by Django 4.2.3 on 2023-07-10 01:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('2605694b-1af5-4502-a36f-dd906d4953bb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]