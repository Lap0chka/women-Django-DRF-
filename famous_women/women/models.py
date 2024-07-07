from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager


class PublishedManger(models.Manager):
    """
    Custom manager to retrieve only published Women instances.
    """
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class Women(models.Model):
    """
    A model representing women with attributes like title, slug, content, creation time, update time, publication status, categories, and tags.
    Methods:
        get_absolute_url: Returns the absolute URL of the woman.
        save: Custom save method to generate a slug if not provided.
        get_categories: Returns a comma-separated list of categories associated with the woman.
    """
    title = models.CharField(max_length=128)
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cat = models.ManyToManyField('Categories', related_name='women')
    tags = TaggableManager(blank=True)
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
        return ", ".join([cat.name for cat in self.cat.all()])

    get_categories.short_description = 'cats'


class Categories(models.Model):
    """
    A model representing categories with attributes like name and slug.
    Methods:
        save: Custom save method to generate a slug if not provided.
    """
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
