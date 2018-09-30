from django.http import HttpResponse
from django.shortcuts import render
from .models import Location, Category, Image

# Create your views here.
def home(request):
    title = 'Home'
    images = Image.get_images()
    image_locations = Location.objects.all()
    return render(request, 'home.html', {'title':title, 'images':images, 'image_locations':image_locations})