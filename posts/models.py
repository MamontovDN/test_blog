from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    """Модель Публикции"""

    author = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(
        verbose_name="дата публикайии", auto_now_add=True
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"

    def __str__(self):
        return self.title
