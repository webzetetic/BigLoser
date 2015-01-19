url(r'^accounts/register/$', 'django_test.views.register_user'),
url(r'^accounts/register_success/$', 'django_test.views.register_success'),

from django.contrib.auth.forms import UserCreationForm

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)