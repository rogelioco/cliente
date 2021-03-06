# Generated by Django 3.0.2 on 2020-02-13 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0003_auto_20200213_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Estado'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='estadoCivil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.EstadoCivil'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Genero'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='ocupacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Ocupacion'),
        ),
    ]
