from django.db import models


# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    img = models.ImageField(upload_to='gallery', null=True, blank=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Галерея"
        verbose_name = "экземпляр"
