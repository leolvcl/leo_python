from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth import get_user_model

# 如果模型是一个代理模型
# 那么就不能在这个模型中添加新的Field

# User.objects.all()
# Person.objects.all()
# 以上两种写法是等价的

# class Person(User):
#     telephone = models.CharField(max_length=11)
#     class Meta:
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)


# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)
#
# @receiver(post_save,sender=User)
# def handler_user_extension(sender,instance,created,**kwargs):
#     if created:
#         UserExtension.objects.create(user=instance)
#     else:
#         instance.extension.save()


class UserManager(BaseUserManager):
    def _create_user(self,telephone,username,password,**kwargs):
        if not telephone:
            raise ValueError('必须要传递手机号码！')
        if not password:
            raise ValueError('必须要传递密码！')
        user = self.model(telephone=telephone,username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username,password=password,**kwargs)

    def create_superuser(self,telephone,username,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone,username=username,password=password,**kwargs)


# class User(AbstractUser):
#     telephone = models.CharField(max_length=11,unique=True)
#     school = models.CharField(max_length=100)
#
#     USERNAME_FIELD = 'telephone'
#
#     objects = UserManager()


class User(AbstractBaseUser,PermissionsMixin):
    telephone = models.CharField(max_length=11,unique=True)
    email = models.CharField(max_length=100,unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

# 切记：
# 如果要自定义User模型
# 那么必须在第一次运行migrate命令之前就先创建好模型


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ('view_article','看文章的权限！')
        ]