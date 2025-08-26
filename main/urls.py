from django.urls import path
from .views import IndexView, post_list, create_post, post_like,post_save

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", post_list, name="post_list"),
    path("posts/new/", create_post, name="create_post"),
    path("posts/<int:post_id>/like/", post_like, name="post_like"),
    path("posts/save/<int:post_id>/", post_save, name="post_save"),


]