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
    categories = models.ManyToManyField('Categories', related_name='women')

    objects = models.Manager()
    published = PublishedManger()

    def get_absolute_url(self):
        return reverse('women:post', args=[self.slug])

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_categories(self):
        return ", ".join([cat.name for cat in self.categories.all()])

    get_categories.short_description = 'Categories'


class Categories(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=164, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()
