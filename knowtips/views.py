from django.shortcuts import render
from django.views.generic import View

# --- BOOTSTRAP ---

class BootstrapView(View):
	template_name = "tips_bootstrap.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class SidebarExampleView(View):
	template_name = "sidebar_example.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class AdaptiveWidthExampleView(View):
	template_name = "adaptivewidth_example.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

class BootstrapStuffExampleView(View):
	template_name = "bootstrapstuff_example.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

# --- DJANGO ---

class DjangoView(View):
	template_name = "tips_django.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

# --- ANDROID ---

class AndroidView(View):
	template_name = "tips_android.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
