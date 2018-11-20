from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from myapp.models import  Item

def index(request):
    return render (request,'myapp/index.html')
