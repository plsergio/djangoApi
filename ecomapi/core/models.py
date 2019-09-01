# coding=utf-8

from django.db import models

class Produto(models.Model):
    name = models.CharField('Nome',max_length=100)
    class Meta:
        verbose_name = 'Nome'
