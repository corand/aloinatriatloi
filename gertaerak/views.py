from django.shortcuts import render
from gertaerak.models import Gertaera
from django.views.generic import DetailView,TemplateView
from dateutil.relativedelta import relativedelta
from datetime import date,timedelta
import calendar
import datetime


class GertaeraView(DetailView):
    slug_field = 'slug'
    model = Gertaera
    context_object_name = "gertaera"
    template_name = "gertaera.html"

    def get_context_data(self, **kwargs):
        context = super(GertaeraView, self).get_context_data(**kwargs)
        context['gertaerak'] = Gertaera.objects.all().order_by('ordua')[:3]
        return context


class Egutegia(TemplateView):
    template_name = "egutegia.html"

    def get_context_data(self, **kwargs):
        context = super(Egutegia, self).get_context_data(**kwargs)

        today = date.today()
        start = date(today.year,today.month,1)
        finish = start + relativedelta(months=1)

        current = start
        next = finish
        prev_month = start - relativedelta(months=1)

        li = []
        while start < finish:
            li.append(start)
            start = start + datetime.timedelta(days=1)

        cal = calendar.Calendar()
        month_days = cal.itermonthdays(today.year, today.month)

        dias = []
        for day in month_days:
            if day == 0:
                dias.append('0')
            else:
                break

        for l in li:
            dias.append(l)



        cont = 0
        calendario = []
        for i in range(0,6):
            fila_cal = []
            for j in range(0,7):
                if len(dias) > cont:
                    fila_cal.append(dias[cont])
                    cont = cont+1
                else:
                    break
            
            calendario.append(fila_cal)

        gertaerak = Gertaera.objects.all().filter(ordua__year=today.year,ordua__month=today.month).order_by('ordua')

        context['calendario'] = calendario
        context['today'] = today
        context['next'] = next
        context['prev'] = prev_month
        context['gertaerak'] = gertaerak
        context['current'] = current
        return context

class EgutegiaParam(TemplateView):
    template_name = "egutegia.html"

    def get_context_data(self, **kwargs):
        context = super(EgutegiaParam, self).get_context_data(**kwargs)
        
        urtea = int(self.kwargs['urtea'])
        hilabetea = int(self.kwargs['hilabetea'])

        today = date.today()
        start = date(urtea,hilabetea,1)
        finish = start + relativedelta(months=1)
        
        current = start
        next = finish
        prev_month = start - relativedelta(months=1)

        li = []
        while start < finish:
            li.append(start)
            start = start + datetime.timedelta(days=1)

        cal = calendar.Calendar()
        month_days = cal.itermonthdays(today.year, today.month)

        dias = []
        for day in month_days:
            if day == 0:
                dias.append('0')
            else:
                break

        for l in li:
            dias.append(l)



        cont = 0
        calendario = []
        for i in range(0,6):
            fila_cal = []
            for j in range(0,7):
                if len(dias) > cont:
                    fila_cal.append(dias[cont])
                    cont = cont+1
                else:
                    break
            
            calendario.append(fila_cal)

        gertaerak = Gertaera.objects.all().filter(ordua__year=urtea,ordua__month=hilabetea).order_by('ordua')

        context['calendario'] = calendario
        context['today'] = today
        context['next'] = next
        context['prev'] = prev_month
        context['gertaerak'] = gertaerak
        context['current'] = current
        return context