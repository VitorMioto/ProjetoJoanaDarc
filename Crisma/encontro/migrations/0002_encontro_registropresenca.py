# Generated by Django 2.2.6 on 2019-10-28 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encontro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encontro',
            name='registroPresenca',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
