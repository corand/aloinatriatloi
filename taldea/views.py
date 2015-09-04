from django.views.generic import TemplateView,CreateView
from gertaerak.models import Gertaera
from esaldiak.models import Esaldi
from bloga.models import Post
from taldea.form import HarremanaForm
import datetime
# Create your views here.

class Index(TemplateView):
    
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        orain = datetime.datetime.now()
        context['gertaerak'] = Gertaera.objects.filter(ordua__gte=orain).order_by('ordua')[:3]
        try:
	    context['post'] = Post.objects.latest('data')
        except Post.DoesNotExist:
            context['post'] = None
        context['esaldi'] = Esaldi.objects.order_by('?').first()
        return context



class Taldea(TemplateView):

    template_name = "taldea.html"

    def get_context_data(self, **kwargs):
        context = super(Taldea, self).get_context_data(**kwargs)
        orain = datetime.datetime.now()
        context['gertaerak'] = Gertaera.objects.filter(ordua__gte=orain).order_by('ordua')[:3]
        context['postak'] = Post.objects.all().order_by('-data')[:3]
        return context

class Harremana(CreateView):
    form_class= HarremanaForm
    template_name = "harremana.html"
    success_url = "bidalita"


class Bidalita(TemplateView):
    template_name = "bidalita.html"
