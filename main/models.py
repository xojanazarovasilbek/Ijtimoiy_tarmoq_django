from django.db import models
from users.models import User

# Action choices
ACTION_CHOICES = (
    ('like', 'Like'),
    ('saved', 'Saved'),
    ('view', 'View')
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    media = models.FileField(upload_to="post_media/", blank=True, null=True)
    likes = models.PositiveBigIntegerField(default=0)
    saveds = models.PositiveBigIntegerField(default=0)
    repost = models.PositiveBigIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.body[:20]}"

class View(models.Model):
    action_type = models.CharField(max_length=30, choices=ACTION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="main_posts")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.action_type} {self.post.id}"

class Notification(models.Model):
    body = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")

    def __str__(self):
        return str(self.body)
