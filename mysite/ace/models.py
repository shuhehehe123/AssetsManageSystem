from django.db import models
#from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Department(models.Model):
    department_name=models.CharField(max_length=20,verbose_name='部门昵称')

    def __str__(self):
        return self.department_name

class Asset(models.Model):
    asset_number=models.CharField(max_length=30,verbose_name='资产编号')
    asset_type=models.CharField(max_length=30,verbose_name='资产分类')
    asset_name=models.CharField(max_length=20,verbose_name='资产名称')
    asset_buyin_time=models.DateTimeField(verbose_name='财务入账日期')
    asset_value=models.CharField(max_length=20,verbose_name='资产价值')
    asset_state=models.CharField(max_length=10,verbose_name='使用情况',blank=True)
    #asset_use_department=models.CharField(max_length=20,verbose_name='使用部门',blank=True)
    asset_use_department=models.ForeignKey(Department,on_delete=models.CASCADE,blank=True)
    #asset_user=models.ForeignKey(lgmodels.User,verbose_name='使用人',blank=True,on_delete=models.CASCADE)
    asset_user=models.CharField(max_length=20,verbose_name='使用人',blank=True)
    asset_count=models.CharField(max_length=20,verbose_name='数量')
    asset_brand=models.CharField(max_length=30,verbose_name='资产品牌',blank=True)
    asset_model=models.CharField(max_length=30,verbose_name='规格型号',blank=True)
    asset_location=models.CharField(max_length=40,verbose_name='资产位置',blank=True)
    asset_comments=models.TextField(blank=True,verbose_name='资产详情')
    class Meta:
        ordering=('-asset_buyin_time',)
    def __str__(self):
        return self.asset_name
    def get_url(self):
        return reverse('ace:asset', kwargs={'pk': self.pk})
    



