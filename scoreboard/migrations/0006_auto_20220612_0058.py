# Generated by Django 3.2 on 2022-06-12 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_auto_20220612_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.team')),
                ('soccerplayer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.soccerplayer')),
            ],
            options={
                'verbose_name_plural': 'Play Games',
            },
        ),
        migrations.AddConstraint(
            model_name='playgame',
            constraint=models.UniqueConstraint(fields=('soccerplayer', 'match', 'position'), name='unique_soccerplayer_match_position'),
        ),
    ]