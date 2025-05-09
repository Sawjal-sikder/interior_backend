# Generated by Django 5.2 on 2025-05-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_review_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=55)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='Latest_Project/')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
