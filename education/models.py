from django.db import models
from config import settings

NULLABLE = {'blank': True, 'null': True}


class Module(models.Model):

    """
    The model of the educational module
    """

    ordinal = models.IntegerField(verbose_name='Serial number')
    name = models.CharField(max_length=100, verbose_name='Course name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    creation_date = models.DateField(auto_now_add=True,
                                     verbose_name='Creation date')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='User', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'
