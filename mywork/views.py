from django.shortcuts import render
from django.views.generic import View

class MegaproyectoView(View):
	template_name = "megaproyecto.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)