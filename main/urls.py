from django.urls import path
from .views import IndexView, post_list, create_post, post_like,add_comment,post_delete,post_detail,post_update

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("posts/", post_list, name="post_list"),
    path("posts/new/", create_post, name="create_post"),
    path("posts/<int:post_id>/like/", post_like, name="post_like"),
    path("post/<int:post_id>/comment/", add_comment, name="add_comment"),
    path("posts/<int:post_id>/",post_detail, name="post_detail"),
    path("posts/<int:post_id>/edit/",post_update, name="post_update"),
    path("posts/<int:post_id>/delete/",post_delete, name="post_delete"),

]