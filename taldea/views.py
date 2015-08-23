from django.views.generic import TemplateView
from gertaerak.models import Gertaera
from esaldiak.models import Esaldi
from bloga.models import Post
# Create your views here.

class Index(TemplateView):
    
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['gertaerak'] = Gertaera.objects.all().order_by('-ordua')[:3]
        context['post'] = Post.objects.latest('data')
        context['esaldi'] = Esaldi.objects.order_by('?').first()
        return context



class Taldea(TemplateView):

    template_name = "taldea.html"

    def get_context_data(self, **kwargs):
        context = super(Taldea, self).get_context_data(**kwargs)
        context['gertaerak'] = Gertaera.objects.all().order_by('-ordua')[:3]
        context['postak'] = Post.objects.all().order_by('-data')[:3]
        return context

class Harremana(TemplateView):

    template_name = "harremana.html"