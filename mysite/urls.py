from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('article/<slug:article_slug>/', ArticleDetailView.as_view(), name='znak'),

]
