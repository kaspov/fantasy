from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from blog.models import Blog

class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'body']

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'body' ] 
    template_name_suffix = '_update_form'

