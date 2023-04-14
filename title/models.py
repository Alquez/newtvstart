from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"