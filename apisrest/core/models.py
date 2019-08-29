#coding=utf-8

from django.db import models

class Music(models.Model):

    class Meta:
        db_table = 'music'

    title = models.CharField(max_length=200)
    seconds = models.IntegerField()

    def __str__(self):
        return self.title

class Chave(models.Model):

    class Meta:
        db_table = 'chave'

    title = models.CharField('Titulo', max_length=100)
    key = models.CharField('Chave', max_length=100)
    app = models.CharField('Aplicação', max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    class Meta:
        db_table = 'produto'

    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return self.nome
