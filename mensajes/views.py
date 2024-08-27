from django.shortcuts import render
from .models import Mensaje

def recibidos(request):
    destinatario = request.GET.get('destinatario', '')

    destinatarios = Mensaje.objects.values_list('destinatario', flat=True).distinct()

    mensajes = Mensaje.objects.filter(destinatario=destinatario) if destinatario else []

    return render(request, 'recibidos.html', {
        'mensajes': mensajes,
        'destinatario': destinatario,
        'destinatarios': destinatarios
    })