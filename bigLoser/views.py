from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from bigLoser.models import Weight, Contest, Contestant
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.template.context import RequestContext
from datetime import timedelta, datetime
from django.contrib.auth.models import User

def index(request):
	if request.user.id == 1:
		return redirect('admin_homepage')
	elif request.user.is_authenticated():
		return redirect('user_homepage', user_id=request.user.id)
	else:
		return redirect('bigLoser_login')

def user_homepage(request, user_id):
	latest_weight_list = Weight.objects.filter(contestant=user_id).order_by('-current_date')[:5]
	user = User.objects.get(id=user_id)
	context = {'latest_weight_list': latest_weight_list, 'user': user}
	return render(request, 'bigLoser/user_homepage.html', context)

def admin_homepage(request):
	return render(request, 'bigLoser/admin_homepage.html')

class WeightCreate(CreateView):
	model = Weight
	fields = ['contestant','current_date','current_weight']
	success_url = reverse_lazy('index')

class ContestCreate(CreateView):
	model = Contest
	fields = ['name','start_date','end_date']
	success_url = reverse_lazy('index')

def render_chart(request, user_id):
    if request.method == "GET":
        series_age = datetime.today() - timedelta(days=90)
        contestant_id = user_id
        qset = Weight.objects\
        	.filter(current_date__gt=series_age, contestant__exact=contestant_id)\
        	.values("current_date", "current_weight")
        weight_json = qset.to_json(labels={},order=("current_date", "current_weight"))
    	return render_to_response("bigLoser/weight_report.html", 
    		{"weight_data": weight_json}, 
    		context_instance=RequestContext(request))
