from django.conf import settings
from django.template import Context, loader


def server_error(request, template_name='500.html'):
	""" http://djangosnippets.org/snippets/1199/ """
	"Always includes MEDIA_URL"
	from django.http import HttpResponseServerError
	t = loader.get_template(template_name)
	return HttpResponseServerError(t.render(Context({'MEDIA_URL': settings.MEDIA_URL})))
