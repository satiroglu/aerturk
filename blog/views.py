from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-createdOn')
    template_name = 'blog/blog.html'

class SinglePost(generic.DetailView):
    model = Post
    template_name = 'blog/single-post.html'