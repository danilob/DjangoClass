# Generated by Django 3.2 on 2022-06-12 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0007_alter_playgame_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playgame',
            name='position',
            field=models.CharField(choices=[('GL', 'Goleiro'), ('LD', 'Lateral Direita'), ('LE', 'Laterial Esquerda'), ('ZA', 'Zagueiro'), ('VL', 'Volante'), ('ME', 'Meia'), ('TK', 'Atacante')], max_length=2),
        ),
    ]
