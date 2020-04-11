from django.db import models


class BaseModel(models.Model):
    """抽象基类
    如无特殊说明，所有实体类均继承于基类
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True)

    class Meta:
        abstract = True