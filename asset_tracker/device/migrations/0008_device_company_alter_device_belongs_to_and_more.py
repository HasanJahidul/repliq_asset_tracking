# Generated by Django 4.2.3 on 2023-07-10 02:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_alter_employee_uid'),
        ('company', '0010_alter_company_uid'),
        ('device', '0007_alter_device_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='company',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='company.company'),
        ),
        migrations.AlterField(
            model_name='device',
            name='belongs_to',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='employee.employee'),
        ),
        migrations.AlterField(
            model_name='device',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('61db5bcc-aedd-44d4-82a2-fdd962337fc8'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
