from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Agent  # Assuming you have an Agent model

def agents(request):
    agnt = Agent.objects.all()
    return render(request, 'agents.html', {'agents': agnt})
