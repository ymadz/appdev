from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def crud(request):
    return render(request, 'crud.html')