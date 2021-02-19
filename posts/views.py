from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from posts.forms import PostForm
from posts.models import Post, User


@login_required
def index(request):
    posts = Post.objects.select_related("author").order_by("-pub_date")
    context = {"page": posts, "title": "Главная страница"}
    return render(request, "index.html", context)


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = user.posts.order_by("-pub_date")
    context = {"page": posts, "title": f"Посты: {username}"}
    return render(request, "index.html", context)


@login_required
def post_edit(request, post_id):
    article = get_object_or_404(Post, id=post_id)
    if article.author != request.user:
        return redirect("index")
    title = " Редактировать публикацию"
    form = PostForm(request.POST or None, instance=article)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("index")
        return render(request, "postForm.html", {"form": form, "title": title})
    return render(request, "postForm.html", {"form": form, "title": title})


@login_required
def new_post(request):
    form = PostForm(request.POST or None)
    title = "Создать Публикацию"
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("index")
        return render(request, "postForm.html", {"form": form, "title": title})
    return render(request, "postForm.html", {"form": form, "title": title})


@method_decorator(login_required(), name="dispatch")
class About(TemplateView):
    template_name = "about.html"
