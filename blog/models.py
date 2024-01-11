from django.db import models

class Post(models.Model):
    
    title = models.CharField(max_length=200)

    body = models.TextField()

    author = models.ForeignKey(
        'auth.user',
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.title