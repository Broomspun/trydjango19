from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .models import Post
from .forms import PostForm


def post_home(request):
    return HttpResponse("<h1>Hello</h1>")


def post_list(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 3)  # Show 3 posts per page

    page = request.GET.get('page')
    queryset = paginator.get_page(page)

    context = {
        "object_list": queryset,
        "title": "List"
    }

    return render(request, "index.html", context)


def post_detail(request, slug): #retrive
    # instance = get_object_or_404(Post, id=3)
    instance = get_object_or_404(Post, slug=slug)
    # instance = get_object_or_404(Post, title__startswith="What")
    context = {
        "title": "Detail",
        "instance": instance
    }

    return render(request, "post_detail.html", context)


def post_create(request):

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "ERROR:  Not Created")

    context = {
        "title": "Create a Post",
        "form": form
    }

    return render(request, "post_create.html", context)


def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Updated", extra_tags="saved")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": "Update Post",
        "form": form,
        "instance": instance
    }

    return render(request, "post_update.html", context)


def post_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Deleted")
    return redirect("index")
