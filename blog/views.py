from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post, Comment
# Create your views here.

# def index(request):
#     return render(request, 'blog/index.html', {})

index = ListView.as_view(model=Post, template_name='blog/index.html')

post_new = CreateView.as_view(model=Post, fields='__all__')

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

post_delete = PostDeleteView.as_view()

comment_new = CreateView.as_view(model=Comment, fields='__all__')