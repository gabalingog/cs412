from django.shortcuts import render
from django.views.generic import ListView
from .models import Voter
import plotly
import plotly.graph_objs as go

# Create your views here.

class VotersListView(ListView):
    '''View to display voters'''

    model = Voter
    template_name = 'voter_analytics/voters.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_queryset(self):
        voters = super().get_queryset().order_by('last_name', 'first_name')

        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party:
                voters = voters.filter(party_affiliation=party)

        if 'min_year' in self.request.GET:
            min_year = self.request.GET['min_year']
            if min_year:
                voters = voters.filter(date_of_birth__year__gte=min_year)

        if 'max_year' in self.request.GET:
            max_year = self.request.GET['max_year']
            if max_year:
                voters = voters.filter(date_of_birth__year__lte=max_year)

        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                voters = voters.filter(voter_score=voter_score)

        if 'v20state' in self.request.GET:
            voters = voters.filter(v20state=True)
        if 'v21town' in self.request.GET:
            voters = voters.filter(v21town=True)
        if 'v21primary' in self.request.GET:
            voters = voters.filter(v21primary=True)
        if 'v22general' in self.request.GET:
            voters = voters.filter(v22general=True)
        if 'v23town' in self.request.GET:
            voters = voters.filter(v23town=True)

        return voters

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['parties'] = Voter.objects.values_list(
            'party_affiliation', flat=True).distinct().order_by('party_affiliation')
        context['years'] = range(1900, 2011)
        context['scores'] = range(0, 6)

        context['sel_party'] = self.request.GET.get('party', '')
        context['sel_min_year'] = self.request.GET.get('min_year', '')
        context['sel_max_year'] = self.request.GET.get('max_year', '')
        context['sel_score'] = self.request.GET.get('voter_score', '')

        params = self.request.GET.copy()
        params.pop('page', None)
        context['query_string'] = params.urlencode()
        return context


class ResultListView(VotersListView):
    '''View to display graphs of aggregate voter data'''

    template_name = 'voter_analytics/graphs.html'
    paginate_by = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        voters = self.get_queryset()
        n = voters.count()

        years = {}
        for v in voters:
            y = v.date_of_birth.year
            years[y] = years.get(y, 0) + 1
        years = dict(sorted(years.items()))

        fig = go.Bar(x=list(years.keys()), y=list(years.values()))
        context['graph_birth_year'] = plotly.offline.plot(
            {'data': [fig],
             'layout_title_text': f'Voter distribution by Year of Birth (n={n})'},
            auto_open=False, output_type='div')

        parties = {}
        for v in voters:
            p = v.party_affiliation.strip()
            parties[p] = parties.get(p, 0) + 1

        fig = go.Pie(labels=list(parties.keys()), values=list(parties.values()))
        context['graph_party'] = plotly.offline.plot(
            {'data': [fig],
             'layout_title_text': f'Voter distribution by Party Affiliation (n={n})'},
            auto_open=False, output_type='div')

        names = ['v20state', 'v21town', 'v21primary', 'v22general', 'v23town']
        counts = [voters.filter(**{name: True}).count() for name in names]

        fig = go.Bar(x=names, y=counts)
        context['graph_elections'] = plotly.offline.plot(
            {'data': [fig],
             'layout_title_text': f'Vote Count by Election (n={n})'},
            auto_open=False, output_type='div')

        return context