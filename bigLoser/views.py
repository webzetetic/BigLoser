from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from bigLoser.models import Weight, Contest, Contestant
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.template.context import RequestContext
from datetime import timedelta, datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

def index(request):
	if request.user.id == 1:
		return redirect('admin_homepage')
	elif request.user.is_authenticated():
		return redirect('user_homepage', user_id=request.user.id)
	else:
		return redirect('bigLoser_login')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()

	return render_to_response('register.html', args)

def register_success(request):
	return render_to_response('register_success.html')

def user_homepage(request, user_id):
	contestant_list = Contestant.objects.filter(user=user_id).order_by('contest')
	user = User.objects.get(id=user_id)
	context = {'user': user, 'contestant_list': contestant_list}
	return render(request, 'bigLoser/user_homepage.html', context)

def contestant_homepage(request, contestant_id):
	latest_weight_list = Weight.objects.filter(contestant=contestant_id).order_by('-current_date')[:5]
	contestant = Contestant.objects.get(id=contestant_id)
	user = contestant.user
	context = {'latest_weight_list': latest_weight_list, 'user': user, 'contestant': contestant}
	return render(request, 'bigLoser/contestant_homepage.html', context)

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

def render_chart(request, contestant_id):
    if request.method == "GET":
        series_age = datetime.today() - timedelta(days=90)
        qset = Weight.objects\
        	.filter(current_date__gt=series_age, contestant__exact=contestant_id)\
        	.values("current_date", "current_weight")
        weight_json = qset.to_json(labels={},order=("current_date", "current_weight"))
    	return render_to_response("bigLoser/weight_report.html", 
    		{"weight_data": weight_json}, 
    		context_instance=RequestContext(request))
