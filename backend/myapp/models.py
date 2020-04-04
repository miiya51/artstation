from django.db import models

# Create your models here.
from django.db import models


class Work(models.Model):
    """作品情報"""
    name = models.CharField(max_length=50)
    createdyear = models.DateTimeField(auto_now_add=False)
    accessionyear = models.DateTimeField(auto_now_add=False)
    createdin = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    imageurl = models.CharField(max_length=200)
    smallimageurl = models.CharField(max_length=200)
    # typeid = models.ForeignKey('Type', on_delete=models.CASCADE)
    updatetime = models.DateTimeField(auto_now_add=False)
    departmentid = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Department(models.Model):
    """作品の種類"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Artist(models.Model):
    """作成者の詳細情報"""
    name = models.CharField(max_length=50)
    begindate = models.DateTimeField(auto_now_add=True)
    EndDate = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class User(models.Model):
    """サイト利用ユーザ情報"""
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """ユーザのコメント情報"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    comment = models.TextField()
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
