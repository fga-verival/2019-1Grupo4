# Generated by Django 2.0.13 on 2019-06-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func_tran', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='func_tran',
            name='compl',
            field=models.CharField(choices=[('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta')], default='B', max_length=6),
        ),
        migrations.AlterField(
            model_name='func_tran',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='func_tran',
            name='tipo_funcoes',
            field=models.CharField(choices=[('EE', 'Entradas Externas'), ('CE', 'Consultas Externas'), ('SE', 'Saídas Externas')], default='EE', max_length=2),
        ),
    ]
