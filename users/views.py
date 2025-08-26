from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.views import View
from django.contrib.auth import logout
from .forms import MyUserCreationForm, MyUserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User,Following
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render
from django.contrib.auth import get_user_model

class UserLogoutView(View):
    def get(self, request):
        return render(request, "registration/logout.html")

    def post(self, request):
        logout(request)
        return redirect("login")

class SignUpView(View):
    def get(self, request):
        form = MyUserCreationForm()
        return render(request, "registration/signup.html", {"form":form})

    def post(self, request):
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "registration/signup.html", {"form": form})

class UserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        form = MyUserChangeForm(instance=request.user)
        return render(request, "registration/user_update.html", {"form": form})

    def post(self, request):
        form = MyUserChangeForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "registration/user_update.html", {"form": form})


class ProfileView(LoginRequiredMixin,View):
    def get(self,request,username):
        user = get_object_or_404(User,username = username)
        is_followed = False
        if Following.objects.filter(user = user,follower=request.user).exists():
            is_followed = True
        return render(request,"profile.html",{"user":user,"is_followed":is_followed})


class FollowView(LoginRequiredMixin,View):
     def post(self,request):
         username = request.POST.get("username")
         redirect_url = request.POST.get("redirect_url")
         user = get_object_or_404(User, username=username)
         following,created = Following.objects.get_or_create(user = user,follower = request.user)
         if not created:
            following.delete()
         return redirect(redirect_url)



User = get_user_model()

def users_list(request):
    users = User.objects.all()
    return render(request, "users_list.html", {"users": users})