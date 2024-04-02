from django.http import JsonResponse

# Create your views here.
def hola_mundo(request):    
    datos =  {"mensaje": "hola_mundo", "curso": "python-django"}
    return JsonResponse(datos)

# 2:44:22