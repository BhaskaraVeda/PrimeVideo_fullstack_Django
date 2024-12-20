from django.db import models

class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=15, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name
