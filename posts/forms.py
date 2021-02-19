from django.forms import ModelForm

from posts.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
        )
        help_texts = {
            "title": "Введите название публикации",
            "text": "Введите любой текст",
        }
