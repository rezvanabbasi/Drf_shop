# Generated by Django 4.2.7 on 2023-12-16 08:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default=uuid.UUID('b776831d-45d7-450d-a1fd-353f7451693f'), max_length=300, verbose_name='uid'),
        ),
    ]
