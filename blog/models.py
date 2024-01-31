from django.db import models
from django.urls import reverse

class Post(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Заголовок")

    body = models.TextField(verbose_name="Основной текст")

    author = models.ForeignKey(
        'auth.user',
        on_delete = models.CASCADE,
        verbose_name="Автор"
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])