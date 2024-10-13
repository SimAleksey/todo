from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(null=True, verbose_name='Слаг')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Автор', related_name='articles',
                               null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'


class Tasks(models.Model):
    description = models.CharField(max_length=100, verbose_name='Описание')
    time = models.TimeField(verbose_name='Время')
    category = models.ForeignKey(Title, on_delete=models.CASCADE, verbose_name='Категория', related_name='tasks')
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.description)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
