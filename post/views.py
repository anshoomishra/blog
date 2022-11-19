from django.shortcuts import render
from django.views.generic import ListView,TemplateView
# Create your views here.

class PostListView(ListView):
    pass

class PostView(TemplateView):
    template_name = "post/home.html"
    

