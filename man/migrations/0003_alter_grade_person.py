# Generated by Django 4.0.10 on 2023-12-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0002_grade_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='person',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='grade_set', to='man.person'),
        ),
    ]
