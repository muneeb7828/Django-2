# Generated by Django 5.2 on 2025-05-13 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_dep_id_employee_dept_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='dept_ID',
            new_name='deptID',
        ),
    ]
