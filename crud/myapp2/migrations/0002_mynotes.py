# Generated by Django 4.2.6 on 2023-12-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('titl', models.CharField(max_length=10)),
                ('myfile', models.FileField(upload_to='Media')),
                ('comments', models.TextField()),
            ],
        ),
    ]
