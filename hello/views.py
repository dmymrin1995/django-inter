from django.shortcuts import render
from .models import slider
# Create your views here.
def index(request):
    obj = slider.objects.all()
    context ={
        'obj':obj
    }

    return render(request, "index.html", context)