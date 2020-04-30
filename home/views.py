from django.shortcuts import render
from reviews.models import Product_Mobile

# Create your views here.

def home(request):
    allMobiles = Product_Mobile.objects.all()
    context = {'allMobiles': allMobiles}
    return render(request, 'home/home.html',context)