from django.shortcuts import render
from django.http import JsonResponse
from graph.models import Database
# Create your views here.
def home(request):
    return render(request, 'home.html')
def index(request):
    return render(request, 'index.html')
 
def temperature_graph(request):
    labels = []
    data = []
 
    queryset = Database.objects.values()
    for entry in queryset:
        labels.append(entry['temperature'])
        data.append(entry['date_added'])
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })