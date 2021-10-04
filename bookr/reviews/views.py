from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "any other random text message"
    return HttpResponse("Hello, {}!" .format(name))

# Create your views here.
