# Generated by Django 5.2 on 2025-05-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_chooseus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('image', models.ImageField(upload_to='gallary/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
