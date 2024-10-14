from django.urls import path
from .views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Zorg ervoor dat deze regel correct is
]
