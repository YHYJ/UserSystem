from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """用户模型"""
    # username = models.CharField(
    #     # _('username'),
    #     max_length=18,
    #     unique=True,
    #     help_text='必填. 不超过18个字符.包含字母,数字和仅有的 @/./+/-/_ only.',
    #     # validators=[username_validator],
    #     error_messages={
    #         'unique': "用户名已被占用",
    #     },
    #     verbose_name='*用户名'
    # )
    nickname = models.CharField(max_length=18, blank=True, verbose_name='昵称')
    # email = models.EmailField(blank=True, verbose_name='*邮箱地址')

    class Meta(AbstractUser.Meta):
        verbose_name = '用户'
        verbose_name_plural = verbose_name
