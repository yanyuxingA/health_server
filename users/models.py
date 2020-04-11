from django.db import models
from service.utils.BaseModels import BaseModel


class Record(BaseModel):
    """用户模型类"""
    user_name = models.CharField(verbose_name='用户名称', max_length=32)
    user_age = models.IntegerField(verbose_name='用户年龄')
    user_temperature = models.FloatField(verbose_name='用户体温')
    user_address = models.CharField(verbose_name='用户地址', max_length=128)

