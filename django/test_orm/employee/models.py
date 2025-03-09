from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=32,verbose_name='姓名')
    email=models.EmailField(verbose_name='邮箱')
    on_delete=models.CASCADE
    dep=models.ForeignKey(to='department',on_delete=models.CASCADE)
    group=models.ManyToManyField(to='group')
    salary=models.DecimalField(max_digits=8,decimal_places=2)
    info=models.OneToOneField(to='employeeinfo',on_delete=models.CASCADE,null=True)
class Department(models.Model)
    dep_name=models.CharField(max_length=32,verbose_name='部门名称')
    dep_script=models.CharField(max_length=60,verbose_name='备注')
class group(models.Model):
    group_name=models.CharField(max_length=32,verbose_name='团队名称')
    group_script = models.CharField(max_length=60, verbose_name='备注')
class Employeeinfo(models.Model):
    phone=models.CharField(max_length=11)
    address=models.EmailField(max_length=50)
