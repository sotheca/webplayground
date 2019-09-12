from django.urls import path
from .views import HiloList, HiloDetail, add_mensaje, start_hilo

mensajero_patterns = ([
	path('', HiloList.as_view(), name='lista_hilo'),
	path('hilo/<int:pk>/', HiloDetail.as_view(), name='detalle_hilo'),
	path('hilo/<int:pk>/add/', add_mensaje, name='add'),
	path('hilo/start/<username>/', start_hilo, name='start'),
], "mensajero")