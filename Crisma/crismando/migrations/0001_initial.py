# Generated by Django 2.2.3 on 2019-07-07 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anoTurma', models.IntegerField()),
                ('ativo', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Turma',
            },
        ),
        migrations.CreateModel(
            name='Crismando',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('dtNascimento', models.DateTimeField()),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('compl', models.CharField(blank=True, max_length=15, null=True)),
                ('nomeMae', models.CharField(max_length=100)),
                ('nomePai', models.CharField(max_length=100)),
                ('telMae', models.CharField(max_length=15)),
                ('telPai', models.CharField(max_length=15)),
                ('fezBatismo', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1)),
                ('fezComunhao', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crismando.Turma')),
            ],
            options={
                'verbose_name_plural': 'Crismando',
            },
        ),
    ]
