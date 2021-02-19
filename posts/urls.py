from django.urls import path

from posts import views

urlpatterns = [
    path("profile/<str:username>/", views.profile, name="profile"),
    path("new/", views.new_post, name="new_post"),
    path("post/<int:post_id>/", views.post_edit, name="post_edit"),
    path("about/", views.About.as_view(), name="about"),
    path("", views.index, name="index"),
]
