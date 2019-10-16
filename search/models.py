from django.db import models

# Create your models here.


class Words(models.Model):
    word = models.CharField(max_length=100)
    frequency = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.word} - {self.frequency}'







