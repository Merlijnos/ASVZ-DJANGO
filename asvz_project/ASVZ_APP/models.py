from django.db import models

class SondepompStatus(models.Model):
    STATUS_TYPES = [
        ('ERROR', 'Fout'),
        ('WARNING', 'Waarschuwing'),
        ('INFO', 'Informatie'),
    ]
    
    status = models.BooleanField()
    timestamp = models.DateTimeField()
    message = models.TextField(default="Geen bericht")
    device_id = models.CharField(max_length=100, default="unknown")
    status_type = models.CharField(max_length=10, choices=STATUS_TYPES, default='INFO')
    is_acknowledged = models.BooleanField(default=False)

    def __str__(self):
        return f"Sondepomp {'Aan' if self.status else 'Uit'} op {self.timestamp}"
