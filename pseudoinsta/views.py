from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post, Comment
from django.views.generic.edit import FormMixin
from .forms import CommentForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class PostListView(ListView):

    model = Post

    paginate_by = 50

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin, DetailView):

    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm
        return context

    template_name = 'pseudoinsta/post_detail.html'

