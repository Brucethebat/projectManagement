from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=65)
    phone = models.CharField(max_length=32)

    def __str__(self):
        return self.name + ' | ' + self.phone