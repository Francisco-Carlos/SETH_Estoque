# Generated by Django 4.1.3 on 2022-12-04 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='Senha',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]