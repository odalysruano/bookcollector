# Generated by Django 4.2.11 on 2024-03-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_review_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='main_app.genre'),
        ),
    ]