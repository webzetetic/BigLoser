from django.shortcuts import render
from django.http import HttpResponse
from bigLoser.models import Weight
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from datetime import timedelta, datetime
from django.db.models import Count

# Create your views here.

def index(request):
	latest_weight_list = Weight.objects.order_by('-current_date')[:5]
	context = {'latest_weight_list': latest_weight_list}
	return render(request, 'bigLoser/index.html', context)

def detail(request, weight_id):
    return HttpResponse("The weight record is %s." % weight_id)

class WeightCreate(CreateView):
	model = Weight
	fields = ['contestant','current_date','current_weight']
	success_url = reverse_lazy('index')

def render_chart(request):
    if request.method == "GET":

        series_age = datetime.today() - timedelta(days=90)

        qset = Weight.objects.filter(current_date__gt=series_age).values("current_date").annotate(Count("id")).order_by()

        weight_json = qset.to_json(labels={"id__count": "Weigh-ins", "current_date": "Date"},
                                 order=("current_date", "id__count"), 
                                 formatting={"id__count": "{0:d} weigh-ins"})

    	return render_to_response("bigLoser/weight_report.html", {"weight_data": weight_json}, context_instance=RequestContext(request))

