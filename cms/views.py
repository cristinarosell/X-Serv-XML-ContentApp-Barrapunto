from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from barrapunto import get_barrapunto


# Create your views here.

noticias_bp=""

def actualizarBp (request):
    global noticias_bp
    noticias_bp = get_barrapunto()
    return HttpResponse ("Actualizando noticias Barrapunto" + noticias_bp)
    
@csrf_exempt
def handler(request, recurso):
    if request.method == "GET":
        try:
            fila = Pages.objects.get(name=recurso)
            salida = fila.page + "</br>" + noticias_bp
            return HttpResponse(salida)
        except Pages.DoesNotExist:
            return HttpResponseNotFound('Pagina no encontrada: /%s.' % recurso)

    elif request.method == "PUT":
        new = Pages(name=recurso, page=request.body)
        new.save()
        return HttpResponse("Guardado")

    else:
        return HttpResponseNotFound("Error en el metodo")
