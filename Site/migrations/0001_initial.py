# Generated by Django 2.1.3 on 2018-11-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, unique=True, verbose_name='Typ strony')),
                ('image', models.ImageField(height_field=250, upload_to='', width_field=500)),
                ('content', models.TextField(verbose_name='Treść')),
                ('last_edit', models.DateTimeField(auto_now=True, verbose_name='Data ostatniej edycji')),
            ],
            options={
                'verbose_name': 'Podstrona',
                'verbose_name_plural': 'Podstrony',
            },
        ),
    ]
