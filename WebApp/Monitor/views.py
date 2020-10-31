from django.shortcuts import render
from django.http import HttpResponse
from Monitor.models import SensorNode, Sensor

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_Sensors = Sensor.objects.all().count()
    num_SensorNodes = SensorNode.objects.all().count()

    context = {
        'num_Sensors': num_Sensors,
        'num_SensorNodes': num_SensorNodes,
    }

    return render(request, 'index.html', context=context)
