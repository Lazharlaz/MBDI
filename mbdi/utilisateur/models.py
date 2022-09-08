from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    manager = 'manager'
    simple = 'simple'
    type_user = [
        (manager, 'manager'), (simple, 'simple')
    ]
    type_profile =models.CharField(max_length=100, choices=type_user, default='simple')

    def __str__(self):
        return self.user.username


class Attente(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=300)
    num = models.CharField(max_length=300)
    longi = models.CharField(max_length=300)
    lati = models.CharField(max_length=300)
    jour = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-jour']


class Fini(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=300)
    num = models.CharField(max_length=300)
    fait_par = models.CharField(max_length=200)
    longi = models.CharField(max_length=300)
    lati = models.CharField(max_length=300)
    jour = models.DateTimeField(auto_now=True)
    fini = models.BooleanField(default=False)
