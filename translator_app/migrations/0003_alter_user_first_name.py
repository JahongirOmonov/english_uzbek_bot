# Generated by Django 5.0.6 on 2024-05-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator_app', '0002_alter_user_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]