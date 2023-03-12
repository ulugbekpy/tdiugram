from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Foydalanuvchi(User):

    class StatusChioce(models.TextChoices):
        STUDENT = 'S'
        TEACHER = 'T'
        GUEST = 'G'

    phone = models.CharField(max_length=15, unique=True)
    status = models.CharField(
        max_length=1, choices=StatusChioce.choices, default=StatusChioce.GUEST)
    image = models.ImageField(upload_to='users/', blank=True, null=True)


class Comment(models.Model):
    sender = models.ForeignKey(Foydalanuvchi, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
