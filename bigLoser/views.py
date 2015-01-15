from django.shortcuts import render
from django.http import HttpResponse
from bigLoser.models import Weight
from django.views.generic.edit import CreateView

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


