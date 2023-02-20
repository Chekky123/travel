from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import ourteam


# Create your views here.

def demo(request):
    obj = place.objects.all()
    obj1= ourteam.objects.all()
    return render(request, "index.html", {'result': obj,'result1': obj1})



# def addition(request):
#  x = int(request.GET['num1'])
# y = int(request.GET['num2'])
# res = x+y
#  return render(request,'result.html',{'result':res})

# ef result(request):
# return render(request,'result.html')
