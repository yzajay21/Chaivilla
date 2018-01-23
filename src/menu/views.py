from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
from .models import Menu_model
# Create your views here.


def item(request, menu_id):
	#template=loader.get_template('menu.html')	
	queryset= Menu_model.objects.filter(category__types=menu_id)
	print (queryset)
	context={
		"items":queryset
	}
	#return render(template,render(context,request))
	return render(request,"menu.html",context)


def Menu_view(request):
	queryset= Menu_model.objects.all()
	#queryset=Menu_model.objects.get(category="Beverages")
	print (queryset)
	model = Menu_model
	context={
		"menu":queryset

	}
	#print (context)
	return render(request,"index.html",context)
