from django.urls import path
from .views import *

urlpatterns = [
    # mapping the url to the view
    path('', RandomArticleView.as_view(), name='random'), # generic class-based view
    path('show_all', ShowAllView.as_view(), name='show_all'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'), # show a single article
    path('article/create', CreateArticleView.as_view(), name='create_article'), # new
]