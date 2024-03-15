from django.db import models

# Create your models here.

from django.db import models


def is_valid(self):
    pass


class Themes(models.Model):
    name = models.CharField(max_length=150, verbose_name='themes_list')
    mavzular = models.CharField(max_length=15000, verbose_name='themes_list')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mavzular'
        verbose_name = 'themes_list'

