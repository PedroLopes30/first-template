from django.db import models
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    email = models.CharField(max_length=200, unique=True, verbose_name="email")
    birth_date = models.DateField()
    age = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
