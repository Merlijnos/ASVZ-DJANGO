import json
import os
from django.shortcuts import render
from django.conf import settings
from .models import SondepompStatus

def dashboard(request):
    # Debug print-statements
    print(f"BASE_DIR: {settings.BASE_DIR}")
    json_file_path = os.path.join(settings.BASE_DIR, 'ASVZ_APP', 'mockdata', 'mock_data.json')
    print(f"JSON file path: {json_file_path}")
    print(f"File exists: {os.path.exists(json_file_path)}")
    
    # Controleer of het bestand bestaat
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"Het bestand {json_file_path} bestaat niet.")

    # Laad mockdata uit JSON-bestand
    with open(json_file_path) as f:
        mock_data = json.load(f)

    # Zet de mockdata om naar SondepompStatus-objecten
    statuses = []
    for item in mock_data:
        status = SondepompStatus(status=item['status'], timestamp=item['timestamp'])
        statuses.append(status)

    return render(request, 'dashboard.html', {'statuses': statuses})