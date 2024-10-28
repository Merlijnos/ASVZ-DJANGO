from django.db import models

class SondepompStatus(models.Model):
    status = models.BooleanField()  # True voor aan, False voor uit
    timestamp = models.DateTimeField()  # Tijdstip van statuswijziging
    message = models.TextField(default="Geen bericht")  # Bericht dat is verzonden
    device_id = models.CharField(max_length=100, default="unknown")  # ID van het apparaat

    def __str__(self):
        return f"Sondepomp {'Aan' if self.status else 'Uit'} op {self.timestamp}"
