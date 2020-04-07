from django.db import models


class PostQuerySet(models.QuerySet):
    def sorted(self):
        return self.order_by('-created_at')


class PostManager(models.Manager):
    def sorted(self):
        return self.get_queryset().sorted()

    def get_queryset(self):
        return PostQuerySet(model=self.model, using=self._db, hints=self._hints)


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = PostManager()

    def __str__(self):
        return self.title
