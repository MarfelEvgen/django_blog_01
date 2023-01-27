from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    class Meta:
        ordering = ['id']


class Tags(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        ordering = ['id']


class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(blank=True, upload_to='photo/women' )
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Famous women'
        ordering = ['-time_create']




