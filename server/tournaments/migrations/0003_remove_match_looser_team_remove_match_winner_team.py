# Generated by Django 5.0.1 on 2024-03-05 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_tournament_group_size_tournament_team_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='looser_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='winner_team',
        ),
    ]
