# Generated by Django 3.2.13 on 2022-06-22 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0007_auto_20220622_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('GL', 'Goleiro'), ('LD', 'Lateral Direita'), ('LE', 'Lateral Esquerda'), ('ZA', 'Zagueiro'), ('VL', 'Volante'), ('ME', 'Meia'), ('TK', 'Atacante')], max_length=2)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.match')),
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
