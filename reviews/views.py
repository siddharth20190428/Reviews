from django.shortcuts import render
from reviews.models import Product_Mobile

# Create your views here.
def reviewsHome(request):
    allMobiles = Product_Mobile.objects.all()
    context = {'allMobiles': allMobiles}
    return render(request, "reviews/reviewsHome.html", context)

def reviewsProduct(request, slug):
    mobile = Product_Mobile.objects.filter(m_slug=slug).first()


    context = {'mobile': mobile}
    return render(request, 'reviews/reviewsProduct.html', context)