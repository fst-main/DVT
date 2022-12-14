# Generated by Django 3.2.4 on 2022-06-02 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=60)),
                ('team_name', models.CharField(max_length=60)),
                ('ticket_number', models.CharField(max_length=60)),
                ('ppi_code', models.CharField(max_length=60)),
                ('user_name', models.CharField(max_length=120)),
                ('email_address', models.EmailField(max_length=120)),
            ],
        ),
    ]
