from django.db import models

# Create your models here.

class TaskModel(models.Model):
    title = models.CharField('标题', max_length=100)
    description = models.TextField('描述')
    completed = models.BooleanField('是否完成', default=False)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'task'


class SellerModel(models.Model):
    name = models.CharField(verbose_name='名称',max_length=100,null=True,blank=True)
    description = models.TextField(verbose_name='描述',null=True,blank=True)
    deliveryTime = models.IntegerField(verbose_name='送达时间',null=True,blank=True)
    score= models.DecimalField(verbose_name='评分',max_digits=4,decimal_places=2,null=True,blank=True)
    serviceScore= models.DecimalField(verbose_name='服务评分',max_digits=4,decimal_places=2,null=True,blank=True)
    foodScore= models.DecimalField(verbose_name='食品评分',max_digits=4,decimal_places=2,null=True,blank=True)
    rankRate= models.DecimalField(verbose_name='好评率',max_digits=4,decimal_places=2,null=True,blank=True)
    minPrice= models.DecimalField(verbose_name='最低配送金额',max_digits=4,decimal_places=2,null=True,blank=True)
    deliveryPrice= models.DecimalField(verbose_name='配送费',max_digits=4,decimal_places=2,null=True,blank=True)
    ratingCount= models.IntegerField(verbose_name='评论数',null=True,blank=True)
    sellCount= models.IntegerField(verbose_name='成交量',null=True,blank=True)
    bulletin = models.TextField(verbose_name='公告',null=True,blank=True)
    avatar = models.ImageField(verbose_name='头像',upload_to='avatar/%Y/%m/',null=True,blank=True)
    pics = models.TextField(verbose_name='商家图片',null=True,blank=True)
    infos = models.TextField(verbose_name='商家营业信息',null=True,blank=True)
    supports = models.TextField(verbose_name='商家优惠信息',null=True,blank=True)

    class Meta:
        db_table = 'seller'