from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PublishedManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Women(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManger()

    def get_absolute_url(self):
        return reverse('women:post', args=[self.slug])

    def save(self):
        self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}'
