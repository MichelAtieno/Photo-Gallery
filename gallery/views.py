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

def new_location(request, pic_location):
    image_locations = Location.objects.all()
    images = Image.filter_by_location(pic_location)
    title = f'{pic_location}'
    return render(request, "location.html",{'images':images, 'title':title, 'image_locations':image_locations})


def search(request):
    image_locations = Location.objects.all()
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        images_found = Image.search_image(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{'message':message, 'images':images_found, 'image_locations':image_locations})
    else:
        message = "No searches yet"
        return render(request, 'search.html', {'message':message, 'image_locations':image_locations})