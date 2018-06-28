from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Tag(models.Model):
    tagname = models.CharField(max_length=16)
    m = models.ManyToManyField(
        to='User',
        through='UserToTag' #使用多对多但定义的表是UserToTag 这样的好处是可以使用m的方法对第三张表进行操作
    )
    def __str__(self):
        return self.tagname

# 对于第三张表 要么自动创建 要么手动创建 不要两边关联起来一起用
class UserToTag(models.Model):
    uid = models.ForeignKey(to='User',on_delete=models.CASCADE)
    tid = models.ForeignKey(to='Tag',on_delete=models.CASCADE)
    ctime = models.DateTimeField(null=True)
    class Meta:
        unique_together=['uid','tid',]