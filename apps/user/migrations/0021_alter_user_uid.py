# Generated by Django 4.2.7 on 2023-12-24 07:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_alter_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default=uuid.UUID('e8cbcbba-043b-4d8f-bb09-22e29acff342'), max_length=300, verbose_name='uid'),
        ),
    ]
