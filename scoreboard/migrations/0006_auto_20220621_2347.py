# Generated by Django 3.2.13 on 2022-06-21 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoccerPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='scoreboard.team')),
            ],
            options={
                'verbose_name_plural': 'SoccerPlayers',
                'ordering': ['name'],
            },
        ),
        migrations.AddConstraint(
            model_name='soccerplayer',
            constraint=models.UniqueConstraint(fields=('team', 'name', 'number'), name='unique_team_name_number'),
        ),
    ]
