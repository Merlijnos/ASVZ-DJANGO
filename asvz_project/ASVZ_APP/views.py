import json
import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
from .models import SondepompStatus
from datetime import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    json_file_path = os.path.join(settings.BASE_DIR, 'ASVZ_APP', 'mockdata', 'mock_data.json')
    
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"Het bestand {json_file_path} bestaat niet.")

    with open(json_file_path) as f:
        mock_data = json.load(f)

    statuses = []
    for item in mock_data:
        timestamp = datetime.fromisoformat(item['timestamp'].replace("Z", "+00:00"))
        status = {
            'status': item['status'],
            'timestamp': timestamp,
            'message': item['message'],
            'device_id': item['device_id']
        }
        statuses.append(status)

    return render(request, 'dashboard.html', {'statuses': statuses})

def get_statuses(request):
    statuses = SondepompStatus.objects.all()
    data = [
        {
            'status': status.status,
            'timestamp': status.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'message': status.message,
            'device_id': status.device_id
        }
        for status in statuses
    ]
    return JsonResponse(data, safe=False)

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log de gebruiker in na registratie
            return redirect('dashboard')  # Verander dit naar de naam van je dashboard-URL
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
