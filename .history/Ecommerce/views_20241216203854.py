from django.http import HttpResponse

def default(request):
    return HttpResponse("<h1>Not Found Page</h1>")