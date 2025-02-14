from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})