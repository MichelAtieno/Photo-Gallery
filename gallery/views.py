from django.http import HttpResponse
from django.shortcuts import render
from .models import Location, Category, Image

# Create your views here.
def home(request):
    title = 'Home'
    images = Image.get_images()
    image_locations = Location.objects.all()
    return render(request, 'home.html', {'title':title, 'images':images, 'image_locations':image_locations})

def single_image(request,image_id,cat_name):
    image_locations = Location.objects.all()

    image = Image.get_image(image_id)

    image_cat = Image.objects.filter(category__category = cat_name)

    title = f'{cat_name}'
    return render(request,"image.html",{'title':title, 'image':image, 'image_cat':image_cat, 'image_locations':image_locations})