from django.db import models

# Create your models here.
#等级
class Level(models.Model):
    title = models.CharField(max_length=16,verbose_name='等级')

    def __str__(self):
        return self.title
#方向
class Direction(models.Model):
    name = models.CharField(max_length=16,verbose_name='名称')

    def __str__(self):
        return self.name
#分类
class Type(models.Model):
    name = models.CharField(max_length=16,verbose_name='类型')

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=32)
    weight = models.IntegerField(verbose_name='权重',default=0)
    level = models.ForeignKey(to='Level',on_delete=models.CASCADE)
    direction = models.ManyToManyField('Direction')
    type = models.ManyToManyField('Type')

    def __str__(self):
        return self.title