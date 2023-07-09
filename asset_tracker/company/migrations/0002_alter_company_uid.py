# Generated by Django 4.2.3 on 2023-07-09 20:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('a6680921-a70f-4158-8874-da31868b527e'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]