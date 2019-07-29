# Generated by Django 2.2.3 on 2019-07-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0003_auto_20190729_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/%Y/%m/', verbose_name='头像'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='bulletin',
            field=models.TextField(blank=True, null=True, verbose_name='公告'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='deliveryPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='配送费'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='deliveryTime',
            field=models.IntegerField(blank=True, null=True, verbose_name='送达时间'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='foodScore',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='食品评分'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='infos',
            field=models.TextField(blank=True, null=True, verbose_name='商家营业信息'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='minPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='最低配送金额'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='pics',
            field=models.TextField(blank=True, null=True, verbose_name='商家图片'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='rankRate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='好评率'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='ratingCount',
            field=models.IntegerField(blank=True, null=True, verbose_name='评论数'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='评分'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='sellCount',
            field=models.IntegerField(blank=True, null=True, verbose_name='成交量'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='serviceScore',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='服务评分'),
        ),
        migrations.AlterField(
            model_name='sellermodel',
            name='supports',
            field=models.TextField(blank=True, null=True, verbose_name='商家优惠信息'),
        ),
    ]
