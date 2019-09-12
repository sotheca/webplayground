from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from .models import Hilo, Mensaje
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class HiloList(TemplateView):
    template_name = "mensajero/hilo_lista.html"

@method_decorator(login_required, name='dispatch')
class HiloDetail(DetailView):
    model = Hilo
    
    def get_object(self):
        obj = super(HiloDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_mensaje(request, pk):
    json_response = {'created':False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            hilo = get_object_or_404(Hilo, pk=pk)
            mensaje = Mensaje.objects.create(user=request.user, contenido=content)
            hilo.mensajes.add(mensaje)
            json_response['created'] = True
            if len(hilo.mensajes.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("Usuario no Autenticado")
    return JsonResponse(json_response)

@login_required
def start_hilo(request, username):
    user = get_object_or_404(User, username=username)
    hilo = Hilo.objects.hallar_or_create(user, request.user)
    return redirect(reverse_lazy('mensajero:detalle_hilo', args=[hilo.pk]))