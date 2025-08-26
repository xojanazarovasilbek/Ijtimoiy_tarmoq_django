from django.shortcuts import render, redirect, get_object_or_404
from django.views import View as DjangoView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post, View as PostAction
from .forms import PostForm
from django.db.models import Q

class IndexView(LoginRequiredMixin, DjangoView):
    def get(self, request):
        posts = Post.objects.all().order_by('-created')
        return render(request, "index.html", {'posts': posts})


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
    posts = Post.objects.all().order_by('-creatred')  # <--- bu yerda to‘g‘riladik
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    PostAction.objects.create(user=request.user, post=post, action_type='like')
    return redirect('index')

@login_required
def post_save(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.saveds += 1
    post.save()
    PostAction.objects.create(user=request.user, post=post, action_type='saved')
    return redirect('index')


    return render(request, "index.html", {'posts': posts, 'query': query})