from django.db import models

# Create your models here.

class Concert(models.Model):
    name = models.CharField(max_length=30, verbose_name = "Название Концерта")
    city = models.CharField(max_length=30, verbose_name = "Город")
    concert_date =  models.DateField(verbose_name = "Дата")
    status = models.CharField(max_length=10, verbose_name = "Статус Концерта")

    def __str__(self):
        return self.name + " " + self.city + " " + str(self.concert_date)

    class meta:
        verbose_name = "Концерт"
        verbose_name_plural = "Концерты"