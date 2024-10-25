from django.urls import path
from .views import dashboard, get_statuses

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Zorg ervoor dat deze regel correct is
    path('api/statuses/', get_statuses, name='get_statuses'),  # Nieuwe URL voor status
]
