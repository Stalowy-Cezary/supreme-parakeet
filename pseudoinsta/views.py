from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostListView(ListView):

    model = Post
    paginate_by = 50

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "pseudoinsta/add_image.html"
    model = Post