

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

from .forms import FeedbackForm, UserCreationForm, CommentForm, CreatePostForm
from .models import BlogPost, Comment, Video


def index(request: WSGIRequest):
    posts = BlogPost.objects.order_by("-id").all()
    return render(request, "index.html", context={"posts": posts})


def post(request: WSGIRequest, id_: int):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = id_
            comment.save()

    blog_post = BlogPost.objects.get(id=id_)
    comments = Comment.objects.filter(post=blog_post).all()
    form = CommentForm()
    return render(request, "post.html", context={"blog_post": blog_post, "form": form, "comments": comments})


def about(request: WSGIRequest):
    return render(request, "about.html", context={"range": range(1, 11)})


def video(request: WSGIRequest):
    videos = Video.objects.all()
    return render(request, "video.html", context={"videos": videos})


def contacts(request: WSGIRequest):
    return render(request, "contacts.html")


@login_required
def profile(request: WSGIRequest):
    if request.method == "POST":
        form = CreatePostForm(data=request.POST, files=request.FILES)
        print(form.fields)
        print(form.is_valid())
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            redirect("index")

    form = CreatePostForm()
    return render(request, "profile.html", context={"form": form})


def signup(request: WSGIRequest):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")

    form = UserCreationForm()
    return render(request, "auth/signup.html", context={"form": form})


def login_(request: WSGIRequest):
    if request.user.is_authenticated:
        return redirect("index")

    success = True
    if request.method == "POST":
        success = False
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user:
                login(request, user)
                return redirect("index")

    form = AuthenticationForm()
    return render(request, "auth/login.html", context={"form": form, "success": success})


@login_required
def logout_(request: WSGIRequest):
    logout(request)
    return redirect("index")


@login_required
def poll(request: WSGIRequest):
    success = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.ip_address = request.META['REMOTE_ADDR']
            feedback.save()
            success = True

    form = FeedbackForm()
    return render(request, "poll.html", context={
        "form": form,
        "post": request.method == "POST",
        "success": success
    })
