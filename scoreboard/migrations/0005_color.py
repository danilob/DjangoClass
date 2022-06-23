# Generated by Django 3.2.13 on 2022-06-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_alter_team_coach'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('definition', models.CharField(max_length=40, unique=True)),
                ('teams', models.ManyToManyField(to='scoreboard.Team')),
            ],
            options={
                'verbose_name_plural': 'Colors',
                'ordering': ['definition'],
            },
        ),
    ]