from django.db import models


# Create your models here.
class District(models.Model):
    district = models.CharField(max_length=250, unique=True)

    class Meta:
        ordering = ('district',)
        verbose_name = 'district'
        verbose_name_plural = 'districts'

    def __str__(self):
        return '{}'.format(self.district)


class Branch(models.Model):
    branch = models.CharField(max_length=250, unique=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        ordering = ('branch',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

    def __str__(self):
        return '{}'.format(self.branch)
