# Generated by Django 4.0.10 on 2023-12-02 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0003_alter_grade_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='person',
        ),
    ]
