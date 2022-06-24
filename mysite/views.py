from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article


# Create your views here.
class ArticleListView(ListView):
    model = Article
    template_name = 'mysite/home.html'
    #context_object_name = 'article'
    slug_url_kwarg = 'article_slug'




class ArticleDetailView(DetailView):
    model = Article
    template_name = "mysite/znaki2.html"
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'


def home(request):
    return render(request, 'home.html')





