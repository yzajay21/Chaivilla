from django.shortcuts import render

# Create your views here.
from django.views.generic.base	import TemplateView
# Create your views here.

class Homepageview(TemplateView):
	template_name='index.html'


class BeverageView(TemplateView):
	template_name='beverages.html'

