from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

class PostList(ListView):   # post_list.html, post-list
    model = Post 
   # template_name = 'blog/index.html' 
    ordering = '-pk' 
    context_object_name = 'post_list'

def about_me(request):
    return render(
        request,
        'blog/aobut-me.html'
    )
    