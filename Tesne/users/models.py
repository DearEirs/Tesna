#!encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserGroup(models.Model):
    """
    用户组
    """
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField('UserProfile')
    permission = models.CharField(u'权限', max_length=50, null=False)

    class Meta:
        verbose_name_plural = "用户组表"

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    """
    用户信息
    """
    name = models.CharField(u'姓名', max_length=32, db_index=True, null=False)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机', max_length=32)
    mobile = models.CharField(u'手机', max_length=32)
    permission = models.ForeignKey(UserGroup, blank=True, null=False, related_name='UserGroup')

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name


