from django.db import models


class PublishedManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Women(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    objects = models.Manager()
    published = PublishedManger()

    def __str__(self):
        return f'{self.title}'
