# Generated by Django 3.2 on 2022-06-12 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_auto_20220612_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tournament', models.CharField(max_length=100)),
                ('goal_home', models.IntegerField(default=0)),
                ('goal_visiting', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'Matchs',
                'ordering': ['-date'],
            },
        ),
        migrations.RemoveConstraint(
            model_name='soccerplayer',
            name='unique_team_name_number_condition',
        ),
        migrations.AddConstraint(
            model_name='soccerplayer',
            constraint=models.UniqueConstraint(fields=('team', 'name', 'number'), name='unique_team_name_number'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_home_team', to='scoreboard.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='team_visiting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_visiting_team', to='scoreboard.team'),
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.UniqueConstraint(fields=('tournament', 'team_home', 'team_visiting'), name='unique_tournament_team_home_visiting'),
        ),
    ]
