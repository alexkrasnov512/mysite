from django.db import models

# Create your models here.
from django.urls import reverse


class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    title = models.CharField(max_length=255, verbose_name="Название знака")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    body = models.TextField(verbose_name="Информация о знаке")
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Картинка")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('znak', kwargs={'article_slug': self.slug})