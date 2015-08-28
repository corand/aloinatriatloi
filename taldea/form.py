from django.forms import ModelForm
from taldea.models import Harremana

class HarremanaForm(ModelForm):
    class Meta:
        model = Harremana
        fields = ['izena', 'emaila', 'textua']