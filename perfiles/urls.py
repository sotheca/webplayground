from django.urls import path
from .views import ProfileListView, ProfileDetailView

perfiles_patterns = ([
	path('', ProfileListView.as_view(), name='lista_perfil'),
	path('<username>/', ProfileDetailView.as_view(), name='detalle_perfil')
], "perfiles")