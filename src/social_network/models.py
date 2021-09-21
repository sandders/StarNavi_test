from django.db import models

from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=80, null=False,
                             blank=False)
    content = models.CharField(max_length=280, null=False, blank=False)
    date_published = models.DateTimeField(
        verbose_name='date published', auto_now_add=True)
    date_updated = models.DateTimeField(
        verbose_name='date updated', auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        unique_together = ('author', 'title')

    def __str__(self):
        return self.title


class Like(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    liked_post = models.ForeignKey(
        'social_network.Post', on_delete=models.CASCADE)
    date_liked = models.DateTimeField(
        verbose_name='date liked', auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'liked_post')

    def __str__(self):
        return f'{self.owner} on {self.liked_post}'


@receiver(pre_save, sender=Post)
def post_pre_save(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.author.username + '-' + instance.title)
