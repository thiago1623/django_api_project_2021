# Generated by Django 3.1.8 on 2021-06-18 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboards', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='score_board',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='scoreboards.scoreboard'),
        ),
    ]
