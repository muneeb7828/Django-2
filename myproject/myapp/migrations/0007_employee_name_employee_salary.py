# Generated by Django 5.2 on 2025-05-13 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_department_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(default=12, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
