from django.http import render

def index(request):
    return render("<h1>Not Found Page</h1>")