from django.shortcuts import render, get_object_or_404
from .models import Project
from blog.models import Post


def home(request):
    projects = Project.objects.all()
    posts = Post.objects.all()

    return render(request, 'home.html', {
        'projects': projects,
        'posts': posts
        })

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, '/blog/templates/post_detail.html', {'post': post})