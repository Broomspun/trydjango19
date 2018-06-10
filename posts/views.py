from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Post


def post_home(request):
    return HttpResponse("<h1>Hello</h1>")


def post_list(request):
    queryset = Post.objects.all()

    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)


def post_detail(request):
    # instance = get_object_or_404(Post, id=3)
    instance = get_object_or_404(Post, title="What is Lorem Ipsum?")
    # instance = get_object_or_404(Post, title__startswith="What")
    context = {
        "title": "Detail",
        "instance": instance
    }

    return render(request, "post_detail.html", context)
