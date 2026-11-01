from django.shortcuts import render
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Result
import plotly
import plotly.graph_objs as go
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

class ResultDetailView(DetailView):
    model = Result
    context_object_name = 'r'
    template_name = 'marathon_analytics/result_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # extract result for single instance
        r = context['r']

        # graph for first half and second half as pie chart
        first_half_seconds = (r.time_half1.hour * 60 + r.time_half1.minute) * 60 + r.time_half1.second
        second_half_seconds = (r.time_half2.hour * 60 + r.time_half2.minute) * 60 + r.time_half2.second

        # plotly
        x = ['first_half_seconds', 'second_half_seconds']
        y = [first_half_seconds, second_half_seconds]

        fig = go.Pie(labels=x, values=y)
        title_text = 'Half Marathon Splits (seconds)'

        # graph as HTML
        graph_div_splits = plotly.offline.plot({'data': [fig],
                                                'layout_title_text': title_text},
                                                auto_open = False,
                                                output_type = 'div')

        context['graph_div_splits'] = graph_div_splits

        return context