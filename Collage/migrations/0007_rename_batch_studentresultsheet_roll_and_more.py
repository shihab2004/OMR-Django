# Generated by Django 5.0.1 on 2024-01-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Collage', '0006_studentresultsheet_analytical_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentresultsheet',
            old_name='batch',
            new_name='roll',
        ),
        migrations.RemoveField(
            model_name='answersheet',
            name='section',
        ),
        migrations.RemoveField(
            model_name='studentresultsheet',
            name='code',
        ),
        migrations.RemoveField(
            model_name='studentresultsheet',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='studentresultsheet',
            name='examiner',
        ),
        migrations.RemoveField(
            model_name='studentresultsheet',
            name='section',
        ),
        migrations.RemoveField(
            model_name='studentresultsheet',
            name='stu_id',
        ),
        migrations.RemoveField(
            model_name='studentresultsheet',
            name='subject',
        ),
    ]
