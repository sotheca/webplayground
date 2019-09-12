from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile

# Create your views here.
class ProfileListView(ListView):
	model = Profile
	template_name = 'perfiles/perfil_lista.html'
	paginate_by = 6

class ProfileDetailView(DetailView): 
	model = Profile
	template_name = 'perfiles/perfil_detalle.html'

	def get_object(self):
		return get_object_or_404(Profile, user__username=self.kwargs['username'])