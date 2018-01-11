from django.shortcuts import render

# Create your views here.
from .models import Menu_model
# Create your views here.


def Menu_view(request):
	queryset= Menu_model.objects.all()
	#queryset=Menu_model.objects.get(category="Beverages")
	#print (queryset)
	model = Menu_model
	context={
	"menu":queryset

	}
#	print (context)
	return render(request,"index.html",context)
# def Menu_view(request):
# 	queryset= Menu_model.objects.filter( category_id=2)
# 	#queryset=Menu_model.objects.get(category="Beverages")
# 	#print (queryset)
# 	model = Menu_model
# 	context={
# 	"menu":queryset

# 	}
# #	print (context)
# 	return render(request,"index.html",context)
def Beverage_view(request):
	queryset= Menu_model.objects.filter( category_id=1)
	#queryset=Menu_model.objects.get(category="Beverages")
	#print (queryset)
	model = Menu_model
	context={
	"menu":queryset

	}
#	print (context)
	return render(request,"beverages.html",context)







def sandwitch_view(request):
	queryset= Menu_model.objects.filter( category_id=2)
	#queryset=Menu_model.objects.get(category="Beverages")
	#print (queryset)
	model = Menu_model
	context={
	"menu":queryset

	}
#	print (context)
	return render(request,"Sandwitches.html",context)


def Desserts_view(request):
	queryset= Menu_model.objects.filter( category_id=3)
	#queryset=Menu_model.objects.get(category="Beverages")
	#print (queryset)
	model = Menu_model
	context={
	"menu":queryset

	}
#	print (context)
	return render(request,"index.html",context)


def MainCourse(request):
	queryset= Menu_model.objects.filter( category_id=4)
	#queryset=Menu_model.objects.get(category="Beverages")
	#print (queryset)
	model = Menu_model
	context={
	"menu":queryset

	}
#	print (context)
	return render(request,"maincourse.html",context)


# def sandwitch_view(request):
# 	#info=Menu_model.objects.raw( SELECT * from Menu_model where category="Sandwitches")
# 	info=Menu_model.objects.filter( category_id=2)
# 	#print (info)
# 	#info=Menu_model.objects.get(category='Sandwitches')
# 	model=Menu_model
# 	context={
# 		"data":info

# 	}
	
# 	print (context)
# 	return render(request,"Sandwitches.html",context)