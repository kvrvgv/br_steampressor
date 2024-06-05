

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=64, verbose_name="Имя")
    email = models.EmailField()
    message = models.TextField(max_length=1024, verbose_name="Сообщение")
    mailing_subscription = models.BooleanField(default=False, verbose_name="Подписка на рассылку")

    created_at = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Краткое содержание")
    content = models.TextField(verbose_name="Полное содержание")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Опубликована")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.ImageField(upload_to=settings.MEDIA_ROOT / 'images', verbose_name="Картинка")

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Опубликован")
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Статья")

    def __str__(self):
        return f"{self.post} - {self.author}"


class Video(models.Model):
    video_file = models.FileField(upload_to=settings.MEDIA_ROOT / "videos")
    name = models.TextField(verbose_name="Название")

    def __str__(self):
        return str(self.name)
