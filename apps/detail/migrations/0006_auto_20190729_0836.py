# Generated by Django 2.2.3 on 2019-07-29 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0005_auto_20190729_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatar/%Y/%m/', verbose_name='头像'),
        ),
    ]