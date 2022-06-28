# 重写USER模型
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self,  username,telephone, password, **kwargs):
        user = self.model( username=username,telephone=telephone, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, telephone, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username, telephone, password, **kwargs)

    def create_superuser(self,  username,telephone, password, **kwargs):
        kwargs['is_superuser'] = True
        return self._create_user( username, telephone,password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    # password,last_login不要重写
    username = models.CharField(max_length=100,unique=True)
    telephone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    gender = models.IntegerField(default=0)  # 0代表未知，1代表男
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    # USERNAME_FIELD：以后再使用authenticate进行验证的时候的字段
    USERNAME_FIELD = 'telephone'
    # 这个属性是用来在命令行中使用createsuperuser命令的时候，会让你输入的字段，这里只要写一个username，以后在创建超级管理员时，会让输入USERNAME_FIELD指定的字段
    # 现在USERNAME_FIELD指定的字段是telephone以及password（password不写也会让你输入）
    REQUIRED_FIELDS = ['username']
    # 以后给某个用户发送邮箱时，会使用这个属性指定的字段的值来发送
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
