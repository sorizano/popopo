from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'webapp/index.html', {})

def blog(request):
    return render(request, 'webapp/blog.html', {})