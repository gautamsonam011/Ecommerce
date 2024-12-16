from django.http import render

def default(request):
    return render("<h1>Not Found Page</h1>")