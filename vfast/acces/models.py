#!encoding=utf-8
from django.db import models

# Create your models here.
class Students(models.Model):
    GENDER_CHOICE = ((1,u'Boy'),(2,u'Girl'))
    name = models.CharField(unique=True,max_length=10,verbose_name=u'姓名')
    age = models.IntegerField(verbose_name=u'年龄')
    gender = models.IntegerField(choices=GENDER_CHOICE,verbose_name=u'性别')
    mobile = models.CharField(unique=True,null=True,max_length=11,verbose_name=u'手机')
    height = models.IntegerField(null=True,verbose_name=u'身高')
    weight = models.IntegerField(null=True,verbose_name=u'体重')
    
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'student'
