from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.urls import reverse

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDeteView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields =['title', 'author', 'summary', 'body']


class BlogUbdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body', 'summary']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class My_view(View):
    def my_view(request):
        target_url = reverse('delete')
        return HttpResponseRedirect(target_url)

# def my_view(request):
#     # Qaytish kerak bo'lgan oynaning URL'ini olish
#     target_url = reverse('target_view_name')  # Target view nomi bilan almashtirilishi kerak
#
#     # HttpResponseRedirect orqali oynadan oynaga qaytish amalga oshiriladi
#     return HttpResponseRedirect(target_url)
