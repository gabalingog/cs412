from django.urls import path
from . import views

urlpatterns = [
    path('', views.VotersListView.as_view(), name='voters'),
    path('graphs', views.ResultListView.as_view(), name='graphs'),
    path('voter/<int:pk>', views.VoterDetailView.as_view(), name='voter'),
]