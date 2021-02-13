from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm
# Create your views here.





class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'