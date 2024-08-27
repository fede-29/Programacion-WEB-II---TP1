from django.db import models

class Mensaje(models.Model):
    remitente = models.CharField(max_length=100)
    destinatario = models.TextField(max_length=100)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"De: {self.remitente} - Para: {self.destinatario}"