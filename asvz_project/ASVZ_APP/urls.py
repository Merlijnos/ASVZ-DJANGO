from django.urls import path
from .views import dashboard, get_statuses, login_view, register, logout_view, get_notifications, acknowledge_notification

urlpatterns = [
    path('', login_view, name='home'),
    path('dashboard/', dashboard, name='dashboard'),  # Zorg ervoor dat deze regel correct is
    path('api/statuses/', get_statuses, name='get_statuses'),  # Nieuwe URL voor status
    path('login/', login_view, name='login'),  # Nieuwe URL voor inloggen
    path('register/', register, name='register'),  # Nieuwe URL voor registratie
    path('logout/', logout_view, name='logout'),  # Nieuwe URL voor uitloggen
    path('api/notifications/', get_notifications, name='get_notifications'),
    path('api/notifications/<int:notification_id>/acknowledge/', acknowledge_notification, name='acknowledge_notification'),
]
