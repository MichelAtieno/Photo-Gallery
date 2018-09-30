from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^image/(?P<cat_name>\w+)/(?P<image_id>\d+)',views.single_image, name='image_gallery'),
    url(r'^location/(?P<pic_location>\d+)', views.new_location, name='filter_location'),
    url(r'^search', views.search, name='search_images')
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)