from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()

	return render_to_response('register/register.html', args)

def register_success(request):
	return render_to_response('register/register_success.html')