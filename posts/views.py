from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post
from .forms import PostForm


def post_home(request):
    return HttpResponse("<h1>Hello</h1>")


def post_list(request):
    queryset = Post.objects.all().order_by("timestamp")

    context = {
        "object_list": queryset,
        "title": "List"
    }

    return render(request, "index.html", context)


def post_detail(request, id): #retrive
    # instance = get_object_or_404(Post, id=3)
    instance = get_object_or_404(Post, id=id)
    # instance = get_object_or_404(Post, title__startswith="What")
    context = {
        "title": "Detail",
        "instance": instance
    }

    return render(request, "post_detail.html", context)


def post_create(request):

    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "title": "Create a Post",
        "form": form
    }

    return render(request, "post_create.html", context)
