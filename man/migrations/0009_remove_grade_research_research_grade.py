# Generated by Django 4.0.10 on 2023-12-02 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('man', '0008_remove_grade_person_grade_research'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='research',
        ),
        migrations.AddField(
            model_name='research',
            name='grade',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='research_set', to='man.grade'),
        ),
    ]
