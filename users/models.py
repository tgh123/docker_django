from django.db import models


# Create your models here.

class Users(models.Model):
    user_name = models.CharField(max_length = 50)
    user_password = models.CharField(max_length = 50)
    user_ticket = models.CharField(max_length = 30, null = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name = '创建时间')
    updated = models.DateTimeField(auto_now = True, verbose_name = '更新时间')

    class Meta:
        db_table = 'users'
