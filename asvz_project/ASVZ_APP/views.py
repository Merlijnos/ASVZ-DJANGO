from django.shortcuts import render
from .models import SondepompStatus

# Create your views here.

def dashboard(request):
    statuses = SondepompStatus.objects.all().order_by('-timestamp')  # Haal alle statusupdates op
    return render(request, 'dashboard.html', {'statuses': statuses})
