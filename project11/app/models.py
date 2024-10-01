from django.db import models

# Create your models here.


class Register(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    add = models.CharField(max_length=50)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"