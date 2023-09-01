from django.db import models


class Infos(models.Model):

    id = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=32)
    pname = models.CharField(max_length=32)
    tname = models.CharField(max_length=32)
    imgsrc = models.CharField(max_length=64)
    mp3 = models.CharField(max_length=64)
    txt = models.CharField(max_length=1000)
class Users(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    userpwd = models.CharField(max_length=32)
class Gedan(models.Model):
    gid = models.AutoField(primary_key=True)
    img = models.CharField(max_length=32)
    nr = models.CharField(max_length=32)
    bfl = models.DecimalField(max_digits=10,decimal_places=0)

class Biaosheng(models.Model):
    bi = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=32)



class Rege(models.Model):
    ri = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=32)

class Xinge(models.Model):
    xi = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=32)


class Xindie(models.Model):
    xd = models.AutoField(primary_key=True)
    img = models.CharField(max_length=32)
    mname = models.CharField(max_length=32)
    zuozhe = models.CharField(max_length=32)

class playlist(models.Model):
    gename=models.CharField(verbose_name='名字',max_length=16)
    singname=models.CharField(verbose_name='名字',max_length=16)
    zhuanname=models.CharField(verbose_name='名字',max_length=16)