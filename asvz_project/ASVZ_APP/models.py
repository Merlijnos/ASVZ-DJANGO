from django.db import models

class SondepompStatus(models.Model):
    status = models.BooleanField()  # True voor aan, False voor uit
    timestamp = models.DateTimeField()  # Tijdstip van statuswijziging

    def __str__(self):
        return f"Sondepomp {'Aan' if self.status else 'Uit'} op {self.timestamp}"
