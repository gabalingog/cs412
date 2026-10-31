from django.shortcuts import render
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from . models import Result
# Create your views here.

class ResultsListView(ListView):
    '''View to display resutls'''

    model = Result
    template_name = 'marathon_analytics/results.html'
    context_object_name = 'results'
    paginate_by = 25
    
    def get_queryset(self):
        results = super().get_queryset()
        # URL to filter
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city:
                results = results.filter(city=city)
        return results