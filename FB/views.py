from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import *
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import reverse


@login_required
def index(request):
    friends = FriendList.objects.filter(user = request.user).values('friend')
    posts = PostsByUser.objects.filter(UID__in=friends).order_by('-updated')
    return render(request, "fb/index.html",{"posts":posts})


class CreatePost(LoginRequiredMixin, View):

    def get(self, request):
        form = CreatePostForm()
        print(form)
        return render(request, "fb/create-post.html",{"form":form})

    def post(self, request):
        user = UserInfo.objects.get(username = request.user)
        PostsByUser.objects.create(UID = user, title = request.POST.get('title'), content = request.POST.get('content'))
        return HttpResponseRedirect(reverse("index"))


class RegisterUser(View):

    def get(self, request):
        return render(request, "registration/register.html")

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        password = request.POST.get('password')
        try:
            UserInfo.objects.create_user(username = username, password=password, first_name=firstname,last_name = lastname, email=email, is_staff = True)
        except Exception as e:
            print(e)
            return render(request, "registration/register.html")
        else:
            return HttpResponseRedirect(reverse("login"))