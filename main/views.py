from django.shortcuts import render, redirect, get_object_or_404
from django.views import View as DjangoView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.db.models import Q

class IndexView(LoginRequiredMixin, DjangoView):
    def get(self, request):
        query = request.GET.get("search", "")
        posts = Post.objects.all().order_by("-created")

        if query:
            posts = posts.filter(
                Q(body__icontains=query) | Q(user__username__icontains=query)
            )

        return render(request, "index.html", {"posts": posts, "query": query})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created')
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('index')


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
    return redirect("index")

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Yangi comment qo‘shish
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comment_form = CommentForm()

    return render(request, "post_detail.html", {
        "post": post,
        "comment_form": comment_form
    })


@login_required
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "post_update.html", {"form": form})


@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        return redirect("index")
    return render(request, "post_delete.html", {"post": post})