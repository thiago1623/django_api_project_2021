# Generated by Django 3.1.8 on 2021-07-09 08:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0003_auto_20210618_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='admins',
            field=models.ManyToManyField(related_name='admins', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
