from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    # mapping the url to the view
    path('', RandomArticleView.as_view(), name='random'), # generic class-based view
    path('show_all', ShowAllView.as_view(), name='show_all'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'), # show a single article
    path('article/create', CreateArticleView.as_view(), name='create_article'), # new
    # specfic key
    path('article/<int:pk>/create_comment', CreateCommentView.as_view(), name='create_comment'),
    path('article/<int:pk>/update', UpdateArticleView.as_view(), name='update_article'),
    path('comment/<int:pk>/delete', DeleteCommentView.as_view(), name='delete_comment'),
    # login
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    # assumes template, so specify
]