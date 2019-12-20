from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name="名称")
    address = models.CharField("地址", max_length=50)
    city = models.CharField("城市", max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    class Meta:
        verbose_name = "出版商"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    aa = models.CharField(max_length=10)

    def __str__(self):
        return self.name
